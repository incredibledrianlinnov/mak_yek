#include <string>
#include <iostream>
#include <pybind11/pybind11.h>
#include <vector>
#include "Board.h"
#include "Engine.h"

namespace py = pybind11;


std::string getBestMovePostion(std::string position, int deep) {
#if _DEBUG 1
    std::cout << "FOR: " << position << std::endl;
#endif // _DEBUG

    Board board(position);
    if (board.GameOver())
    {
        return position;
    }

    Move bestMove = Engine::GetBestMove(board, deep);

    Board newPosition(board, bestMove);
    newPosition.Mirror();

    return newPosition.ToString();
}



PYBIND11_MODULE(checkers_bot_cpp, m) {
    m.doc() = "checkers c++ bot";

    m.def("get_best_move_position", &getBestMovePostion);
}