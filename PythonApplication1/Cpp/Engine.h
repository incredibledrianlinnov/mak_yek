#pragma once

#include "Board.h"


struct Engine
{
	static int EvaluatePosition(Board& board);
	static Move GetBestMove(Board board, int deep);

private:
	static int AlphaBeta(Board& board, int deep, int alpha, int beta, bool isMaximisingPlayer);
};
