# 사용자에게 가위, 바위, 보 중 하나를 물어봅니다.
# 사용자가 가위, 바위, 보를 고르면, 컴퓨터도 같이 가위, 바위, 보를 내고 승패를 가릅니다.
# 다합쳐 3번을 지거나, 3번을 이기면 게임은 최종 스코어를 보여 주면서 끝이 납니다.
# 힌트
#
# 리스트를 한 개를 사용하고 사용자의 입력을 받아야 합니다.
# 앞서 사용했던 임의 뽑기를 다시 사용합니다. 검색 키워드 : random, randint, shuffle
# 컴퓨터에게 가위, 바위, 보의 승패를 가르쳐줘야 합니다.
# 마감시간
#
# 필수 과제가 아닙니다.
# 이번 주 일요일 18:00 이후 제 깃허브에 해답을 공유 하겠습니다.


# 랜덤 임포트
import random

# 게임 시작?
play = input("시작해볼까?[Y/N]")
if play == "Y":
    play = True
    print("게임을 시작합니다.")
elif play == "N":
    play = False
    print("게임을 취소합니다.")
else:
    print("Y/N을 입력하세요")

while play = True


