#include "Board.h"
#include <stdexcept>

Board::Board(const std::string& position)
{
	if (position.size() != 32)
	{
		throw std::invalid_argument("position size != 32");
	}

	for (int i = 0; i < position.size(); i++)
	{
		switch (position[i])
		{
		case 'p':
			blackPawns.set(i * 2 + (i / 4 + 1) % 2);
			break;
		case 'q':
			blackQueens.set(i * 2 + (i / 4 + 1) % 2);
			break;
		case 'P':
			whitePawns.set(i * 2 + (i / 4 + 1) % 2);
			break;
		case 'Q':
			whiteQueens.set(i * 2 + (i / 4 + 1) % 2);
			break;
		}
	}
}

Board::Board(const Board& board, const Move& move)
{
	bool isPawnMove = board.whitePawns.get(move.GetFrom());
	if (isPawnMove) {
		if (move.GetTo().row() == 0)
		{
			this->whitePawns = board.whitePawns - move.GetFrom();
			this->whiteQueens = board.whiteQueens | move.GetTo().as_board();
		}
		else
		{
			this->whitePawns = (board.whitePawns - move.GetFrom()) | move.GetTo().as_board();
			this->whiteQueens = board.whiteQueens;
		}

	}
	else {
		this->whiteQueens = board.whiteQueens - move.GetFrom();
		this->whiteQueens = this->whiteQueens | move.GetTo().as_board();
		this->whitePawns = board.whitePawns;
	}
	
	this->blackPawns = board.blackPawns - move.killed;
	this->blackQueens = board.blackQueens - move.killed;

	Mirror();
}

std::vector<Move> Board::GetPosibleMoves()
{
	std::vector<Move> result;
	result.reserve(60); //TODO MAY CHANGE

	//pawns
	for (auto source : whitePawns) {
		//left
		if (BoardSquare::IsValidCoord(source.col() - 1)) {
			BoardSquare dest(source.row() - 1, source.col() - 1);
			if (!blackPices().get(dest) && !whitePices().get(dest))
			{
				result.push_back(Move(source, dest));
			}
			else if (BoardSquare::IsValid(source.row() - 2, source.col() - 2))
			{
				BoardSquare jump(source.row() - 2, source.col() - 2);
				if (blackPices().get(dest) && !blackPices().get(jump) && !whitePices().get(jump)) {
					addKills(result, Move(source, jump, dest));
				}
			}
		}

		//right
		if (BoardSquare::IsValidCoord(source.col() + 1)) {
			BoardSquare dest(source.row() - 1, source.col() + 1);
			if (!blackPices().get(dest) && !whitePices().get(dest))
			{
				result.push_back(Move(source, dest));
			}
			else if (BoardSquare::IsValid(source.row() - 2, source.col() + 2))
			{
				BoardSquare jump(source.row() - 2, source.col() + 2);
				if (blackPices().get(dest) && !blackPices().get(jump) && !whitePices().get(jump)) {
					addKills(result, Move(source, jump, dest));
				}
			}
		}
	}

	//queens
	for (auto source : whiteQueens) {
		//right down
		BoardSquare dest(source);
		int8_t dx = 1, dy = 1;

		while (true)
		{
			if (BoardSquare::IsValid(dest.row() + dy, dest.col() + dx))
			{
				dest = BoardSquare(dest.row() + dy, dest.col() + dx);

				if (!blackPices().get(dest) && !whitePices().get(dest))
				{
					result.push_back(Move(source, dest));
				}
				else if (BoardSquare::IsValid(dest.row() + dy, dest.col() + dx))
				{
					BoardSquare jump(dest.row() + dy, dest.col() + dx);
					if (blackPices().get(dest) && !blackPices().get(jump) && !whitePices().get(jump))
					{
						addQueenKills(result, Move(source, jump, dest));
					}
					break;
				}
				else {
					break;
				}
			}
			else {
				break;
			}
		}

		//right up
		dest = source;
		dx = 1, dy = -1;

		while (true)
		{
			if (BoardSquare::IsValid(dest.row() + dy, dest.col() + dx))
			{
				dest = BoardSquare(dest.row() + dy, dest.col() + dx);

				if (!blackPices().get(dest) && !whitePices().get(dest))
				{
					result.push_back(Move(source, dest));
				}
				else if (BoardSquare::IsValid(dest.row() + dy, dest.col() + dx))
				{
					BoardSquare jump(dest.row() + dy, dest.col() + dx);
					if (blackPices().get(dest) && !blackPices().get(jump) && !whitePices().get(jump))
					{
						addQueenKills(result, Move(source, jump, dest));
					}
					break;
				}
				else {
					break;
				}
			}
			else {
				break;
			}
		}

		//left down
		dest = source;
		dx = -1, dy = 1;

		while (true)
		{
			if (BoardSquare::IsValid(dest.row() + dy, dest.col() + dx))
			{
				dest = BoardSquare(dest.row() + dy, dest.col() + dx);

				if (!blackPices().get(dest) && !whitePices().get(dest))
				{
					result.push_back(Move(source, dest));
				}
				else if (BoardSquare::IsValid(dest.row() + dy, dest.col() + dx))
				{
					BoardSquare jump(dest.row() + dy, dest.col() + dx);
					if (blackPices().get(dest) && !blackPices().get(jump) && !whitePices().get(jump))
					{
						addQueenKills(result, Move(source, jump, dest));
					}
					break;
				}
				else {
					break;
				}
			}
			else {
				break;
			}
		}

		//left up
		dest = source;
		dx = -1, dy = -1;

		while (true)
		{
			if (BoardSquare::IsValid(dest.row() + dy, dest.col() + dx))
			{
				dest = BoardSquare(dest.row() + dy, dest.col() + dx);

				if (!blackPices().get(dest) && !whitePices().get(dest))
				{
					result.push_back(Move(source, dest));
				}
				else if (BoardSquare::IsValid(dest.row() + dy, dest.col() + dx))
				{
					BoardSquare jump(dest.row() + dy, dest.col() + dx);
					if (blackPices().get(dest) && !blackPices().get(jump) && !whitePices().get(jump))
					{
						addQueenKills(result, Move(source, jump, dest));
					}
					break;
				}
				else {
					break;
				}
			}
			else {
				break;
			}
		}
	}

	return result;
}

std::string Board::ToString()
{
	std::string result;
	for (int i = 0; i < 32; i++)
	{
		BoardSquare square(i * 2 + (i / 4 + 1) % 2);
		auto y = square.as_int() / 8;
		auto x = square.as_int() % 8;
		if (blackPawns.get(square))
		{
			result += 'p';
		}
		else if (blackQueens.get(square))
		{
			result += 'q';
		}
		else if (whitePawns.get(square))
		{
			result += 'P';
		}
		else if (whiteQueens.get(square))
		{
			result += 'Q';
		}
		else {
			result += '*';
		}
	}
	return result;
}

void Board::Mirror()
{
	std::swap(this->whitePawns, this->blackPawns);
	this->whitePawns.Mirror();
	this->blackPawns.Mirror();

	std::swap(this->whiteQueens, this->blackQueens);
	this->whiteQueens.Mirror();
	this->blackQueens.Mirror();
}

bool Board::GameOver()
{
	return whitePices().count() == 0 || blackPices().count() == 0 || !haveMove();
}

void Board::addKills(std::vector<Move>& moves, Move previous)
{
	bool add = true;
	BitBoard blackPices(this->blackPices() - previous.killed);
	BitBoard whitePices(this->whitePices() - previous.GetFrom());
	
	//left
	if (BoardSquare::IsValid(previous.GetTo().row() - 2, previous.GetTo().col() - 2)) {
		BoardSquare kill(previous.GetTo().row() - 1, previous.GetTo().col() - 1);
		BoardSquare jump(previous.GetTo().row() - 2, previous.GetTo().col() - 2);
		if (blackPices.get(kill) && !blackPices.get(jump) && !whitePices.get(jump))
		{
			add = false;
			addKills(moves, Move(previous, jump, kill));
		}
	}
	
	//right
	if (BoardSquare::IsValid(previous.GetTo().row() - 2, previous.GetTo().col() + 2)) {
		BoardSquare kill(previous.GetTo().row() - 1, previous.GetTo().col() + 1);
		BoardSquare jump(previous.GetTo().row() - 2, previous.GetTo().col() + 2);
		if (blackPices.get(kill) && !blackPices.get(jump) && !whitePices.get(jump))
		{
			add = false;
			addKills(moves, Move(previous, jump, kill));
		}
	}


	if (add) {
		moves.push_back(previous);
	}
}

void Board::addQueenKills(std::vector<Move>& moves, Move previous)
{
	bool add = true;
	BitBoard blackPices(this->blackPices() - previous.killed);
	BitBoard whitePices(this->whitePices() - previous.GetFrom());

	//right down
	BoardSquare dest(previous.GetTo());
	int8_t dx = 1, dy = 1;

	while (true)
	{
		if (BoardSquare::IsValid(dest.row() + dy, dest.col() + dx))
		{
			dest = BoardSquare(dest.row() + dy, dest.col() + dx);

			if (whitePices.get(dest) || blackPices.get(dest))
			{
				if (blackPices.get(dest))
				{
					if (BoardSquare::IsValid(dest.row() + dy, dest.col() + dx))
					{
						BoardSquare jump(dest.row() + dy, dest.col() + dx);
						if (!blackPices.get(jump) && !whitePices.get(jump))
						{
							add = false;
							addQueenKills(moves, Move(previous, jump, dest));
						}
					}
				}
				break;
			}
		}
		else {
			break;
		}
	}

	//right up
	dest = previous.GetTo();
	dx = 1, dy = -1;

	while (true)
	{
		if (BoardSquare::IsValid(dest.row() + dy, dest.col() + dx))
		{
			dest = BoardSquare(dest.row() + dy, dest.col() + dx);

			if (whitePices.get(dest) || blackPices.get(dest))
			{
				if (blackPices.get(dest))
				{
					if (BoardSquare::IsValid(dest.row() + dy, dest.col() + dx))
					{
						BoardSquare jump(dest.row() + dy, dest.col() + dx);
						if (!blackPices.get(jump) && !whitePices.get(jump))
						{
							add = false;
							addQueenKills(moves, Move(previous, jump, dest));
						}
					}
				}
				break;
			}
		}
		else {
			break;
		}
	}

	//left down
	dest = previous.GetTo();
	dx = -1, dy = 1;

	while (true)
	{
		if (BoardSquare::IsValid(dest.row() + dy, dest.col() + dx))
		{
			dest = BoardSquare(dest.row() + dy, dest.col() + dx);

			if (whitePices.get(dest) || blackPices.get(dest))
			{
				if (blackPices.get(dest))
				{
					if (BoardSquare::IsValid(dest.row() + dy, dest.col() + dx))
					{
						BoardSquare jump(dest.row() + dy, dest.col() + dx);
						if (!blackPices.get(jump) && !whitePices.get(jump))
						{
							add = false;
							addQueenKills(moves, Move(previous, jump, dest));
						}
					}
				}
				break;
			}
		}
		else {
			break;
		}
	}

	//left up
	dest = previous.GetTo();
	dx = -1, dy = -1;

	while (true)
	{
		if (BoardSquare::IsValid(dest.row() + dy, dest.col() + dx))
		{
			dest = BoardSquare(dest.row() + dy, dest.col() + dx);

			if (whitePices.get(dest) || blackPices.get(dest))
			{
				if (blackPices.get(dest))
				{
					if (BoardSquare::IsValid(dest.row() + dy, dest.col() + dx))
					{
						BoardSquare jump(dest.row() + dy, dest.col() + dx);
						if (!blackPices.get(jump) && !whitePices.get(jump))
						{
							add = false;
							addQueenKills(moves, Move(previous, jump, dest));
						}
					}
				}
				break;
			}
		}
		else {
			break;
		}
	}

	if (add) {
		moves.push_back(previous);
	}
}

bool Board::haveMove()
{

	//pawns
	for (auto source : whitePawns) {
		//left
		if (BoardSquare::IsValidCoord(source.col() - 1)) {
			BoardSquare dest(source.row() - 1, source.col() - 1);
			if (!blackPices().get(dest) && !whitePices().get(dest))
			{
				return true;
			}
			else if (BoardSquare::IsValid(source.row() - 2, source.col() - 2))
			{
				BoardSquare jump(source.row() - 2, source.col() - 2);
				if (blackPices().get(dest) && !blackPices().get(jump) && !whitePices().get(jump)) {
					return true;
				}
			}
		}

		//right
		if (BoardSquare::IsValidCoord(source.col() + 1)) {
			BoardSquare dest(source.row() - 1, source.col() + 1);
			if (!blackPices().get(dest) && !whitePices().get(dest))
			{
				return true;
			}
			else if (BoardSquare::IsValid(source.row() - 2, source.col() + 2))
			{
				BoardSquare jump(source.row() - 2, source.col() + 2);
				if (blackPices().get(dest) && !blackPices().get(jump) && !whitePices().get(jump)) {
					return true;
				}
			}
		}
	}

	//queens
	for (auto source : whiteQueens) {
		//right down
		BoardSquare dest(source);
		int8_t dx = 1, dy = 1;

		while (true)
		{
			if (BoardSquare::IsValid(dest.row() + dy, dest.col() + dx))
			{
				dest = BoardSquare(dest.row() + dy, dest.col() + dx);

				if (!blackPices().get(dest) && !whitePices().get(dest))
				{
					return true;
				}
				else if (BoardSquare::IsValid(dest.row() + dy, dest.col() + dx))
				{
					BoardSquare jump(dest.row() + dy, dest.col() + dx);
					if (blackPices().get(dest) && !blackPices().get(jump) && !whitePices().get(jump))
					{
						return true;
					}
					break;
				}
				else {
					break;
				}
			}
			else {
				break;
			}
		}

		//right up
		dest = source;
		dx = 1, dy = -1;

		while (true)
		{
			if (BoardSquare::IsValid(dest.row() + dy, dest.col() + dx))
			{
				dest = BoardSquare(dest.row() + dy, dest.col() + dx);

				if (!blackPices().get(dest) && !whitePices().get(dest))
				{
					return true;
				}
				else if (BoardSquare::IsValid(dest.row() + dy, dest.col() + dx))
				{
					BoardSquare jump(dest.row() + dy, dest.col() + dx);
					if (blackPices().get(dest) && !blackPices().get(jump) && !whitePices().get(jump))
					{
						return true;
					}
					break;
				}
				else {
					break;
				}
			}
			else {
				break;
			}
		}

		//left down
		dest = source;
		dx = -1, dy = 1;

		while (true)
		{
			if (BoardSquare::IsValid(dest.row() + dy, dest.col() + dx))
			{
				dest = BoardSquare(dest.row() + dy, dest.col() + dx);

				if (!blackPices().get(dest) && !whitePices().get(dest))
				{
					return true;
				}
				else if (BoardSquare::IsValid(dest.row() + dy, dest.col() + dx))
				{
					BoardSquare jump(dest.row() + dy, dest.col() + dx);
					if (blackPices().get(dest) && !blackPices().get(jump) && !whitePices().get(jump))
					{
						return true;
					}
					break;
				}
				else {
					break;
				}
			}
			else {
				break;
			}
		}

		//left up
		dest = source;
		dx = -1, dy = -1;

		while (true)
		{
			if (BoardSquare::IsValid(dest.row() + dy, dest.col() + dx))
			{
				dest = BoardSquare(dest.row() + dy, dest.col() + dx);

				if (!blackPices().get(dest) && !whitePices().get(dest))
				{
					return true;
				}
				else if (BoardSquare::IsValid(dest.row() + dy, dest.col() + dx))
				{
					BoardSquare jump(dest.row() + dy, dest.col() + dx);
					if (blackPices().get(dest) && !blackPices().get(jump) && !whitePices().get(jump))
					{
						return true;
					}
					break;
				}
				else {
					break;
				}
			}
			else {
				break;
			}
		}
	}

	return false;
}
