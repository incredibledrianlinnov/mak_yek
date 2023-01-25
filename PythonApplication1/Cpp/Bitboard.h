#pragma once

#include <cstdint>
#include <cassert>
#include <string>
#include "bititer.h"

using namespace lczero;

class BoardSquare {
public:
    constexpr BoardSquare() {}
    constexpr BoardSquare(std::uint8_t num) : square_(num) {}
    constexpr BoardSquare(int row, int col) : BoardSquare(row * 8 + col) {}

    constexpr std::uint8_t as_int() const { return square_; }

    constexpr std::uint64_t as_board() const { return 1ULL << square_; }

    void set(int row, int col) { square_ = row * 8 + col; }

    int row() const { return square_ / 8; }

    int col() const { return square_ % 8; }

    void Mirror() { square_ = square_ ^ 0b111000; }

    static bool IsValidCoord(int x) { return x >= 0 && x < 8; }

    static bool IsValid(int row, int col) {
        return IsValidCoord(row) && IsValidCoord(col);
    }

    constexpr bool operator==(const BoardSquare& other) const {
        return square_ == other.square_;
    }

    constexpr bool operator!=(const BoardSquare& other) const {
        return square_ != other.square_;
    }

private:
    std::uint8_t square_ = 0;
};

class BitBoard {
public:
    constexpr BitBoard(std::uint64_t board) : board_(board) {}
    BitBoard() = default;
    BitBoard(const BitBoard&) = default;
    BitBoard& operator=(const BitBoard&) = default;

    std::uint64_t as_int() const { return board_; }
    void clear() { board_ = 0; }

    // Counts the number of set bits in the BitBoard.
    int count() const {
#if defined(NO_POPCNT)
        std::uint64_t x = board_;
        x -= (x >> 1) & 0x5555555555555555;
        x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333);
        x = (x + (x >> 4)) & 0x0F0F0F0F0F0F0F0F;
        return (x * 0x0101010101010101) >> 56;
#elif defined(_MSC_VER) && defined(_WIN64)
        return _mm_popcnt_u64(board_);
#elif defined(_MSC_VER)
        return __popcnt(board_) + __popcnt(board_ >> 32);
#else
        return __builtin_popcountll(board_);
#endif
    }

    // Like count() but using algorithm faster on a very sparse BitBoard.
    // May be slower for more than 4 set bits, but still correct.
    // Useful when counting bits in a Q, R, N or B BitBoard.
    int count_few() const {
#if defined(NO_POPCNT)
        std::uint64_t x = board_;
        int count;
        for (count = 0; x != 0; ++count) {
            // Clear the rightmost set bit.
            x &= x - 1;
        }
        return count;
#else
        return count();
#endif
    }

    // Sets the value for given square to 1 if cond is true.
    // Otherwise does nothing (doesn't reset!).
    void set_if(BoardSquare square, bool cond) { set_if(square.as_int(), cond); }
    void set_if(std::uint8_t pos, bool cond) {
        board_ |= (std::uint64_t(cond) << pos);
    }
    void set_if(int row, int col, bool cond) {
        set_if(BoardSquare(row, col), cond);
    }

    // Sets value of given square to 1.
    void set(BoardSquare square) { set(square.as_int()); }
    void set(std::uint8_t pos) { board_ |= (std::uint64_t(1) << pos); }
    void set(int row, int col) { set(BoardSquare(row, col)); }

    // Sets value of given square to 0.
    void reset(BoardSquare square) { reset(square.as_int()); }
    void reset(std::uint8_t pos) { board_ &= ~(std::uint64_t(1) << pos); }
    void reset(int row, int col) { reset(BoardSquare(row, col)); }

    // Gets value of a square.
    bool get(BoardSquare square) const { return get(square.as_int()); }
    bool get(std::uint8_t pos) const {
        return board_ & (std::uint64_t(1) << pos);
    }
    bool get(int row, int col) const { return get(BoardSquare(row, col)); }

    // Returns whether all bits of a board are set to 0.
    bool empty() const { return board_ == 0; }

    // Checks whether two bitboards have common bits set.
    bool intersects(const BitBoard& other) const { return board_ & other.board_; }

    // Flips black and white side of a board.
    void Mirror() { board_ = ReverseBitsInBytes(ReverseBytesInBytes(board_)); }

    bool operator==(const BitBoard& other) const {
        return board_ == other.board_;
    }

    bool operator!=(const BitBoard& other) const {
        return board_ != other.board_;
    }

    BitIterator<BoardSquare> begin() const { return board_; }
    BitIterator<BoardSquare> end() const { return 0; }

    std::string DebugString() const {
        std::string res;
        for (int i = 7; i >= 0; --i) {
            for (int j = 0; j < 8; ++j) {
                if (get(i, j))
                    res += '#';
                else
                    res += '.';
            }
            res += '\n';
        }
        return res;
    }

    // Applies a mask to the bitboard (intersects).
    BitBoard& operator&=(const BitBoard& a) {
        board_ &= a.board_;
        return *this;
    }

    friend void swap(BitBoard& a, BitBoard& b) {
        using std::swap;
        swap(a.board_, b.board_);
    }

    // Returns union (bitwise OR) of two boards.
    friend BitBoard operator|(const BitBoard& a, const BitBoard& b) {
        return { a.board_ | b.board_ };
    }

    // Returns intersection (bitwise AND) of two boards.
    friend BitBoard operator&(const BitBoard& a, const BitBoard& b) {
        return { a.board_ & b.board_ };
    }

    // Returns bitboard with one bit reset.
    friend BitBoard operator-(const BitBoard& a, const BoardSquare& b) {
        return { a.board_ & ~(b.as_board()) };
    }

    // Returns difference (bitwise AND-NOT) of two boards.
    friend BitBoard operator-(const BitBoard& a, const BitBoard& b) {
        return { a.board_ & ~b.board_ };
    }

private:
    std::uint64_t board_ = 0;
};

struct Move
{
    BitBoard killed;

    Move() = default;
    constexpr Move(BoardSquare from, BoardSquare to) : data_(to.as_int() + (from.as_int() << 6)) {}
    constexpr Move(BoardSquare from, BoardSquare to, BitBoard killed) : data_(to.as_int() + (from.as_int() << 6)), killed(killed) {};
    constexpr Move(BoardSquare from, BoardSquare to, BoardSquare killed) : data_(to.as_int() + (from.as_int() << 6)), killed(killed.as_board()) {};
    Move(BoardSquare from, BoardSquare to, BitBoard killed, BoardSquare extraKill) : data_(to.as_int() + (from.as_int() << 6)), killed(killed | extraKill.as_board()) {};
    Move(const Move& move, BoardSquare to, BoardSquare extraKill) : data_(to.as_int() + (move.GetFrom().as_int() << 6)), killed(move.killed | extraKill.as_board()) {};

    BoardSquare GetTo() const { return BoardSquare(data_ & kToMask); }
    BoardSquare GetFrom() const { return BoardSquare((data_ & kFromMask) >> 6); }

    void SetTo(BoardSquare to) { data_ = (data_ & ~kToMask) | to.as_int(); }
    void SetFrom(BoardSquare from) {
        data_ = (data_ & ~kFromMask) | (from.as_int() << 6);
    }

    void AddKill(BoardSquare position) { killed = killed | position.as_board(); }
    void RemoveKill(BoardSquare position) { killed = killed & ~position.as_board(); }

private:
    uint16_t data_;

    enum Masks : uint16_t {
        kToMask = 0b0000000000111111,
        kFromMask = 0b0000111111000000,
    };
};