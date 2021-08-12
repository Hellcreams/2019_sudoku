from copy import deepcopy

error = 0
def error_reset():
    global error
    error = 0

def across(board):
    global error
    board_check = deepcopy(board)
    for _ in range(6) :
        for none in range(6) :
            if 0 in board_check[_] :
                board_check[_].remove(0)
        if len(board_check[_]) != len(set(board_check[_])) :
            print("가로", _+1,"번째 줄에 오류가 있습니다.")
            error += 1

def down(board):
    global error
    board_check = deepcopy(board)
    for _ in range(6) :
        i = [board_check[__][_] for __ in range(6)]
        for none in range(6) :
            if 0 in i :
                i.remove(0)
        if len(i) != len(set(i)) :
            print("세로", _+1,"번째 줄에 오류가 있습니다.")
            error += 1

def tile_left(board):
    global error
    board_check = deepcopy(board)
    for _, __, in zip(range(0, 6, 2), range(1, 6, 2)) :
        i = [*[board_check[_][___] for ___ in range(3)], *[board_check[__][___] for ___ in range(3)]]
        for none in range(6):
            if 0 in i :
                i.remove(0)
        if len(i) != len(set(i)) :
            print("타일", _+1,"번째 줄에 오류가 있습니다.")
            error += 1
def tile_right(board):
    global error
    board_check = deepcopy(board)
    for _, __, in zip(range(0, 6, 2), range(1, 6, 2)) :
        i = [*[board_check[_][___] for ___ in range(3, 6)], *[board_check[__][___] for ___ in range(3, 6)]]
        for none in range(6) :
            if 0 in i :
                i.remove(0)
        if len(i) != len(set(i)) :
            print("타일", __+1,"번째 줄에 오류가 있습니다.")
            error += 1
        
def zero(board):
    global error
    i0 = 0
    for _ in range(6) :
        for __ in range(6) :
            if board[_][__] == 0 :
                i0 += 1
    if i0 != 0 :
        print("빈칸이 존재합니다. 개수 :", i0)
        error += 1

def number(board):
    global error
    i_out = 0
    for _ in range(6) :
        for __ in range(6) :
            if not 0 <= board[_][__] <= 6 :
                i_out += 1
    if i_out != 0 :
        print("유효하지 않은 숫자가 존재합니다. 개수 :", i_out)
        error += 1

if __name__ == "__main__" :
    print("스도쿠 검사 class")
    input()
