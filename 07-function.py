#Function
# input parameter, return
# 입력값 반환값에 따라 4개지 경우로 나뉨


#함수는 def로 시작함
def say_hello(name):
    print("hi, {}".format(name))


name1 = "marco"
name2 = "jane"
name3 = "john"
name4 = "tom"


say_hello(name1)
say_hello(name2)
say_hello(name3)
say_hello(name4)

# print("hello, {}".format(name1))
# print("hello, {}".format(name2))
# print("hello, {}".format(name3))
# print("hello, {}".format(name4))
# 함수는 중복되는 내용들을 단순하게 조정 가능함

# 입력값o 반환값o


def sum(a, b):
    return a+b

# 입력값o 반환값x


def say_hello (name):
    print("hi, {}".format(name))


# 입력값X 반환값o
def return_1():
    return 1


# 입력값X 반환값x
def hello_world():
    print("hello world")

