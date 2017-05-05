package main

import (
    "os"
    "fmt"
    "strconv"
)

/*
board structure is represented as an array
column = index
line = board[index]
*/

func try_queen(n int, board []int) (int) {
    count := 0
    for line := 0; line < n; line++ {
        board_new_queen := append(board, line)
        if verify(board_new_queen) {
            if len(board_new_queen) == n {
                count++
            } else {
                count += try_queen(n, board_new_queen)
            }
        }
    }
    return count
}

func verify(board []int) (bool) {
    last_col := len(board) - 1
    last_line := board[last_col]
    for col := 0; col < last_col; col++ {
        line := board[col]
        if line == last_line || abs(last_line - line) == abs(last_col - col) {
            return false
        }
    }
    return true
}

func abs(i int) (int) {
    if i < 0 {
        return -i
    } else {
        return i
    }
}

func main() {
    n := 8
    if len(os.Args) > 1 {
        if i, err := strconv.Atoi(os.Args[1]); err == nil {
            n = i
        }
    }
    board := make([]int, n)
    count := try_queen(n, board[:0])
    fmt.Println(count)
}
