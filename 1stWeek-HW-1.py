#-*- coding: utf-8 -*-
# 구현 내용
#
# 처음 파이썬 파일을 실행 시키면, 한식, 중식, 일식 중 한 가지를 고르라는 내용이 나옵니다.
# 그 중에서 한 가지를 고르면 식당 이름을 하나 임의로 추천해 줍니다.
# 힌트
#
# 리스트를 여러 개 사용하고 사용자의 입력을 받아야 합니다.
# 마감시간
#
# 이번 주 일요일 18:00
# 마감 시간 종료 후 제 깃허브에 해답을 공유 하겠습니다.

import random

#음식점 list
korea_food = ['한1식당', '한2식당', '한3식당', '한4식당']
china_food = ['중1식당', '중2식당', '중3식당']
japan_food = ['일1식당', '일2식당']

#restaurant 변수 초기화

restaurant = "default"

# 사용자 선택값 입력
choose = input("한식, 일식, 중식 중 하나를 고르시오. ")

if choose == "한식":
    restaurant = korea_food #입력 변수가 한식 이면 korea_food 입력
elif choose == "중식":
    restaurant = china_food
elif choose == "일식":
    restaurant = japan_food
else : #입력 이상한거 하면 오류 문구 출력
    print("세개중 하나를 정확하게 입력해야지")

# 음식점 list 갯수 count
y = len(restaurant)
# random값 입력
x = random.randrange(0,y)


#입력받은 음식 종류 출력
print("당신은 "+choose+"를 선택하셨습니다.")
#식당 랜덤 값 입력하여 출력
print(restaurant[x])
