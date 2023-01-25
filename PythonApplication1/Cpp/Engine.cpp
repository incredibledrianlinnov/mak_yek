#include <algorithm>
#include <iostream>
#include <chrono>
#include "Engine.h"

#define INFINITY INT_MAX
#define WIN 100000

#define QUEEN_COST 30

static const int8_t kWhitePawnRowScore[] = {
	30,
	20,
	17,
	15,
	13,
	10,
	10,
	10
};

static const int8_t kBlackPawnRowScore[] = {
	-10,
	-10,
	-10,
	-13,
	-15,
	-17,
	-20,
	-30
};

int Engine::EvaluatePosition(Board& board)
{
	if (board.blackPices().count() == 0)
		return WIN;
	
	if (board.whitePices().count() == 0)
		return -WIN;

	if (!board.haveMove())
		return 0;

	int score = 0;

	//white
	for (auto square : board.whitePawns) {
		score += kWhitePawnRowScore[square.row()];
	}
	for (auto square : board.whiteQueens) {
		score += QUEEN_COST;
	}

	//black
	for (auto square : board.blackPawns) {
		score += kBlackPawnRowScore[square.row()];
	}
	for (auto square : board.blackQueens) {
		score -= QUEEN_COST;
	}


	return score;
}

Move Engine::GetBestMove(Board board, int deep)
{
#if _DEBUG 1
	auto start = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::system_clock::now().time_since_epoch());
#endif // _DEBUG 1
	int bestMoveScore = -INFINITY;
	Move bestMove;

	for (Move& move : board.GetPosibleMoves()) {
		Board newPosition(board, move);
#if _DEBUG 1
		auto pos = newPosition.ToString();
		std::cout << pos << std::endl;
#endif // _DEBUG 1
		int value = AlphaBeta(newPosition, deep, -INFINITY, INFINITY, false);
#if _DEBUG 1
		std::cout << value << std::endl;
#endif // _DEBUG 1
		if (value >= bestMoveScore)
		{
			bestMoveScore = value;
			bestMove = move;
		}
	}
#if _DEBUG 1
	std::cout << "time = " << (std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::system_clock::now().time_since_epoch()) - start).count() << "ms" << std::endl << std::endl;
#endif // _DEBUG 1
	return bestMove;
}

int Engine::AlphaBeta(Board& board, int deep, int alpha, int beta, bool isMaximisingPlayer)
{
	if (deep == 0 || board.GameOver())
	{
		int value = EvaluatePosition(board) * (isMaximisingPlayer ? 1 : -1);
		if (value == WIN)
		{
			return value + deep;
		}
		else if (value == -WIN) 
		{
			return value - deep;
		}
		return value;
	}

	int bestMoveValue = isMaximisingPlayer ? -INFINITY : INFINITY;

	if (isMaximisingPlayer)
	{
		for (auto& move : board.GetPosibleMoves()) {
			Board newPosition(board, move);

			bestMoveValue = std::max(bestMoveValue, AlphaBeta(newPosition, deep - 1, alpha, beta, !isMaximisingPlayer));
			alpha = std::max(alpha, bestMoveValue);
			if (beta < alpha)
			{
				break;
			}
		}
	}
	else
	{
		for (auto& move : board.GetPosibleMoves())
		{
			Board newPosition(board, move);
			bestMoveValue = std::min(bestMoveValue, AlphaBeta(newPosition, deep - 1, alpha, beta, !isMaximisingPlayer));
			beta = std::min(beta, bestMoveValue);
			if (beta < alpha)
			{
				break;
			}
		}
	}
	return bestMoveValue;
}
