# 방금 배운 클래스를 복습해 봅시다.
# 학교 클래스를 만들어주세요.
# 학교 클래스는 이름, 설립연도, 주소라는 정보를 가지고 있어야 합니다.
# 클래스를 활성화 할 때, 위의 3가지 데이터를 반드시 입력하도록 처리해 봅시다.


class School:

    def __init__(self, name, year, address):
        self.name = name
        self.year = year
        self.address = address


sc_name_1 = input("name")
sc_year_1 = input("year")
sc_address_1 = input("address")


school_1 = School(sc_name_1, sc_year_1, sc_address_1)
print(school_1.name)
print(school_1.year)
print(school_1.address)