from source import quest
from source import check
from copy import deepcopy

def checking(board):
    check.across(board)
    check.down(board)
    check.tile_left(board)
    check.tile_right(board)

##문제를 선택하고 버그를 방지하는 파트
print("6x6 스도쿠 게임에 오신 것을 환영합니다!\n")
quest.substitute()

board = deepcopy(quest.solve)
quest.modifable(board)
checking(board)
check.number(board)
if check.error != 0 :
    print("\n다음과 같은 오류가 있어 문제를 풀 수 없습니다.")
    input("문제를 확인하시고 게임을 재실행하세요. 엔터를 누르면 게임이 종료됩니다.")
    quit()
check.zero(board)
if check.error == 0 :
    print("\n빈칸이 존재하지 않아 문제를 풀 수 없습니다.")
    input("문제를 확인하시고 게임을 재실행하세요. 엔터를 누르면 게임이 종료됩니다.")
    quit()
check.error_reset()

print("\n[문제]")
for _ in range(6):
    print(board[_])
print("가로와 세로에 0을 입력하여 게임을 일시중단할 수 있습니다.")

##문제를 푸는 파트
while True :
    while True : #대입하는 파트
        num = int(input("숫자 : "))
        down = int(input("가로 : ")) - 1
        across = int(input("세로 : ")) - 1

        if across == down == -1 :
            print("게임을 일시중단하였습니다.")
            break
        elif str(across)+str(down) in quest.non_modify :
            print("해당 값은 바꿀 수 없습니다.")
        elif -1 < num < 7 and -1 < across < 6 and -1 < down < 6 :
            board[across][down] = num
            for _ in range(6):
                print(board[_])
        else : print("유효하지 않은 입력입니다.")
    while True : #다른 옵션을 선택하는 파트
        print("q 를 입력하여 게임을 종료합니다.")
        print("con 을 입력하여 게임을 계속합니다.")
        print("com 을 입력하여 문제와 현재 풀이를 비교합니다.")
        print("reset 을 입력하여 게임을 다시 시작합니다.")
        print("check 를 입력하여 정답인지 확인합니다.")
        pause = input("입력 : ")
        if pause == 'q' or pause == 'Q':
            quit()
        elif pause == 'con' :
            break
        elif pause == 'com' :
            print("[원본]")
            for _ in range(6):
                print(quest.solve[_])
            print("[현재 풀이]")
            for _ in range(6):
                print(board[_])
        elif pause == 'reset':
            board = deepcopy(quest.solve)
            print("게임을 다시 시작합니다.")
            for _ in range(6):
                print(board[_])
            break
        elif pause == 'check':
            checking(board)
            check.zero(board)
            if check.error == 0 :
                check.error -= 1
                break
            check.error_reset()
            for _ in range(6):
                print(board[_])
            print("다시 한 번 풀어볼까요?")
            break
        else : print("잘못된 입력입니다.")
    if check.error == -1 : #정답인지 확인하고 종료하는 파트
        print("\n정답을 맞추셨습니다! 와아-")
        print("[원본]")
        for _ in range(6):
            print(quest.solve[_])
        print("[정답]")
        for _ in range(6):
            print(board[_])
        input("축하드립니다! 엔터를 누르시면 게임을 종료합니다.")
        quit()
