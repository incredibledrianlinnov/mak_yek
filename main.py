import sys
from hashlib import sha256
import json
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from models.board import FigureType
from game import Game
from registration import Ui_MainWindow as reg_window
from user import Ui_MainWindow as private_window
import pygame

import checkers_bot_cpp as Game_AI

DEFAULT_POSITION = 'pppppppp****************PPPPPPPP'


def init_private():
    main_window = QtWidgets.QMainWindow()
    ui = private_window()
    ui.setupUi(main_window)
    ui.pushButton_exit.clicked.connect(log_out)
    return main_window, ui


def show_hide():
    if authorization_ui.checkBox.isChecked():
        authorization_ui.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
    else:
        authorization_ui.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)


def init_authorization():
    main_window = QtWidgets.QMainWindow()
    ui = reg_window()
    ui.setupUi(main_window)
    ui.pushButton.clicked.connect(authorization)
    ui.pushButton_reg.clicked.connect(register)
    ui.checkBox.stateChanged.connect(show_hide)
    return main_window, ui


def log_in(user):
    authorization_window.hide()
    lk_window.setWindowTitle(user['username'])
    lk_ui.label_account_name.setText(user['username'])
    lk_ui.wins.setText(str(user['wins']))
    lk_ui.loses.setText(str(user['loses']))
    lk_ui.pushButton_old.setEnabled(bool(user['current_game']))

    def play_friend():
        play(DEFAULT_POSITION, False)

    def play_AI():
        play(DEFAULT_POSITION, True)

    def continue_game():
        play(user['current_game'], user['current_game_mode'] == 'AI')

    lk_ui.pushButton_new_game_friend.clicked.connect(play_friend)
    lk_ui.pushButton_new_game_ai.clicked.connect(play_AI)
    lk_ui.pushButton_old.clicked.connect(continue_game)
    lk_window.show()


def log_out():
    lk_window.hide()
    authorization_window.show()


def register():
    username = authorization_ui.lineEdit_name.text()
    password = authorization_ui.lineEdit_pass.text()
    if not username or not password:
        error = QMessageBox(authorization_window)
        error.setWindowTitle("Ошибка\t\t\t\t\t")
        error.setText("Вы не заполнили данные для регистрации")
        error.exec()
        return
    if get_user_by_name(username):
        error = QMessageBox(authorization_window)
        error.setWindowTitle("Ошибка\t\t\t\t\t")
        error.setText("Такой пользователь уже существует")
        error.exec()
        return
    user = create_user(username, password)
    authorization_ui.lineEdit_name.setText('')
    authorization_ui.lineEdit_pass.setText('')
    log_in(user)


def authorization():
    username = authorization_ui.lineEdit_name.text()
    password = authorization_ui.lineEdit_pass.text()
    if not username or not password:
        error = QMessageBox(authorization_window)
        error.setWindowTitle("Ошибка\t\t\t\t\t")
        error.setText("Введите данные для авторизации")
        error.exec()
        return
    user = get_user_by_name(username)
    if not user:
        error = QMessageBox(authorization_window)
        error.setWindowTitle("Ошибка\t\t\t\t\t")
        error.setText("Такого пользователя не существует")
        error.exec()
        return
    if user['password'] == sha256(password.encode('utf-8')).hexdigest():
        authorization_ui.lineEdit_name.setText('')
        authorization_ui.lineEdit_pass.setText('')
        log_in(user)
        return
    else:
        error = QMessageBox(authorization_window)
        error.setWindowTitle("Ошибка\t\t\t\t\t")
        error.setText("Неверный пароль пользователя")
        error.exec()
        return


def get_user_by_name(username):
    for user in get_users():
        if username == user['username']:
            return user
    return None


def create_user(username: str, password: str) -> dict:
    user = {
        'username': username,
        'password': sha256(password.encode('utf-8')).hexdigest(),
        'wins': 0,
        'loses': 0,
        'current_game': None,
        'current_game_mode': 'AI'
    }
    users = get_users()
    users.append(user)
    with open('users.json', "w", encoding='utf-8') as file:
        json.dump(users, file)

    return user


def get_users():
    if os.path.exists('users.json'):
        with open('users.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        return []


def play(position: str, AI: bool):
    game = Game(position)

    cell_size = 80
    background = pygame.image.load('images/back.png')

    white = pygame.image.load('images/White.png')
    black = pygame.image.load('images/Black.png')
    white_queen = pygame.image.load('images/WhiteQueen.png')
    black_queen = pygame.image.load('images/BlackQueen.png')

    move_img = pygame.image.load('images/move.png')

    pygame.init()
    screen = pygame.display.set_mode([640, 640])
    running = True

    selected = None
    moves = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                in_game_pos = (pos[0] // cell_size, pos[1] // cell_size)
                if selected is None:
                    if int(game.get_figure_at(in_game_pos[0], in_game_pos[1])) < 1 or int(
                            game.get_figure_at(in_game_pos[0], in_game_pos[1])) % 2 == game.board.turn:
                        continue
                    selected = in_game_pos
                    moves = game.get_moves_for(selected[0], selected[1])
                else:
                    move = None
                    for m in moves:
                        if m.position_to == in_game_pos:
                            move = m
                            break
                    if move:
                        game.move(move)
                        if AI:
                            game.ai_move(Game_AI.get_best_move_position(game.board.to_string(True), 7),
                                         True)  # TODO change to ne 10
                    selected = None
                    moves = []

        screen.blit(background, background.get_rect())
        for x in range(8):
            for y in range(8):
                if game.get_figure_at(x, y) == FigureType.White:
                    screen.blit(white, (x * cell_size, y * cell_size))
                elif game.get_figure_at(x, y) == FigureType.WhiteQueen:
                    screen.blit(white_queen, (x * cell_size, y * cell_size))
                elif game.get_figure_at(x, y) == FigureType.Black:
                    screen.blit(black, (x * cell_size, y * cell_size))
                elif game.get_figure_at(x, y) == FigureType.BlackQueen:
                    screen.blit(black_queen, (x * cell_size, y * cell_size))

        for move in moves:
            screen.blit(move_img, (move.position_to[0] * cell_size, move.position_to[1] * cell_size))

        pygame.display.update()


app = QtWidgets.QApplication(sys.argv)
authorization_window, authorization_ui = init_authorization()
lk_window, lk_ui = init_private()
authorization_window.show()
sys.exit(app.exec())
