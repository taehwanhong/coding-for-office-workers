# 과제 2 - 회사 조직도 만들기
#
# 구현 내용
#
# 사람 클래스를 하나 만듭니다. 사람의 기본 요소는 이름, 나이, 성별로 합시다.
# 직장 동료 클래스를 사람 클래스를 이용해서 만듭시다. 사람 기본 요소 외 별도의 추가 사항은 직급입니다.
# 힌트
#
# 클래스와 상속을 활용합니다.
# 사람의 기본 요소인 이름, 나이, 성별은 각각 새로운 사람을 만들 때, 입력을 받을 수 있도록 합시다.
# 직장 동료의 기본 직급은 "대리"로 지정합니다.
# (고급) 사람 클래스에서 새로운 사람을 만들 때 입력은 그대로 유지하면서,
# 직급도 처음 만들어질 때 입력하도록 변경을 도전해봅시다.
#
# 마감시간
#
# 이번 주 일요일 18:00
# 마감 시간 종료 후 제 깃허브에 해답을 공유 하겠습니다.


# 사람 만들기, 왠지 딕셔너리가 쓰고싶다. 이름,나이,성별,직급으로 구성해보자
person1 = {"name":"dname", "age":"dage", "sex":"dsex", "position":"대리"}

# Person class 만들기,
class Person:
    # person1의 이름 나이 성별을 input값으로 채운다.
    person1['name'] = input("name?")
    person1['age'] = input("age?")
    person1['sex'] = input("sex?")


# 잘 채워졌나?
print(person1)


# 동료 클래스 만들기, Person class inherited
class Colleague(Person):
    # 포지션 입력받기
    person1['position'] = input("position?")

print(person1)