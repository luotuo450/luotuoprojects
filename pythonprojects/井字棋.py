import math

# 定义棋盘
board = [" " for _ in range(9)]


# 打印棋盘
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


# 检查胜利条件
def check_win(board, player):
    win_conditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],  # 行
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],  # 列
        [0, 4, 8],
        [2, 4, 6],  # 对角线
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False


# 检查棋盘是否已满
def is_full(board):
    return " " not in board


# 评估函数
def evaluate_board(board):
    if check_win(board, "X"):
        return 1
    elif check_win(board, "O"):
        return -1
    else:
        return 0


# Minimax算法 with Alpha-Beta剪枝
def minimax(board, depth, alpha, beta, maximizing_player):
    if check_win(board, "X"):
        return 1
    if check_win(board, "O"):
        return -1
    if is_full(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = minimax(board, depth + 1, alpha, beta, False)
                board[i] = " "
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                eval = minimax(board, depth + 1, alpha, beta, True)
                board[i] = " "
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval


# AI选择最佳落子位置
def ai_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, 0, -math.inf, math.inf, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move


# 主函数
def main():
    print("欢迎来到井字棋游戏！")
    print_board(board)
    while True:
        player_move = int(input("请输入你的落子位置 (0-8): "))
        if board[player_move] != " ":
            print("该位置已有棋子，请重新输入")
            continue
        board[player_move] = "O"
        print_board(board)
        if check_win(board, "O"):
            print("你赢了！")
            break
        if is_full(board):
            print("平局！")
            break
        ai_move_index = ai_move(board)
        board[ai_move_index] = "X"
        print("AI落子:")
        print_board(board)
        if check_win(board, "X"):
            print("AI赢了！")
            break
        if is_full(board):
            print("平局！")
            break


if __name__ == "__main__":
    main()
