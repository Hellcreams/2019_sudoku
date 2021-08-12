solve = 0
quests = {}
non_modify = []

def __init__():
    pass

def substitute():
    global solve
    print("문제 이름들 : ", list(quests.keys()))
    solve = quests[input("문제 이름을 입력하세요. : ")]

def modifable(board):
    for _ in range(6):
        for __ in range(6):
            if board[_][__] != 0 :
                non_modify.append(str(_)+str(__))

#복붙해서 문제 만들기
#변수의 숫자와 키가 일치하도록 바꾼 후 문제를 만드세요.
q0 = [_ for _ in range(6)]
q0[0] = [0, 0, 0, 0, 0, 0]
q0[1] = [0, 0, 0, 0, 0, 0]
q0[2] = [0, 0, 0, 0, 0, 0]
q0[3] = [0, 0, 0, 0, 0, 0]
q0[4] = [0, 0, 0, 0, 0, 0]
q0[5] = [0, 0, 0, 0, 0, 0]
quests['zero'] = q0

q1 = [_ for _ in range(6)]
q1[0] = [7, 8, 9, 6, 5, 1]
q1[1] = [0, 0, 0, 4, 3, 2]
q1[2] = [0, 0, 0, 0, 0, 0]
q1[3] = [0, 0, 0, 0, 0, 0]
q1[4] = [0, 0, 0, 0, 0, 0]
q1[5] = [0, 0, 0, 0, 0, 0]
quests['out'] = q1

q2 = [_ for _ in range(6)]
q2[0] = [0, 2, 3, 0, 5, 6]
q2[1] = [4, 5, 0, 1, 2, 0]
q2[2] = [2, 0, 1, 6, 0, 5]
q2[3] = [6, 4, 5, 0, 3, 1]
q2[4] = [3, 0, 2, 5, 6, 4]
q2[5] = [5, 6, 0, 0, 1, 0]
quests['non_zero'] = q2

if __name__ == '__main__' :
    print("문제 class")
    print("리스트 :", list(quests.keys()))
