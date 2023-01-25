#pragma once

#include "Bitboard.h"
#include <string>
#include <vector>

struct Board
{
	BitBoard whitePawns;
	BitBoard whiteQueens;

	BitBoard blackPawns;
	BitBoard blackQueens;

	BitBoard whitePices() const { return whitePawns | whiteQueens; }
	BitBoard blackPices() const { return blackPawns | blackQueens; }


	Board(const std::string& position);
	Board(const Board& board, const Move& move);

	std::vector<Move> GetPosibleMoves();
	std::string ToString();

	void Mirror();
	bool GameOver(); 
	bool haveMove();

private:
	void addKills(std::vector<Move>& moves, Move previous);
	void addQueenKills(std::vector<Move>& moves, Move previous);
};
