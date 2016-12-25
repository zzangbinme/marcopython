# 회사 조직도 만들기

class Company:
    name = str()
    age = int()
    sex = str()
    position = str()

    def __init__(self):
        self.name = input("이름을 입력하세요.")
        self.age = int(input("나이를 입력하세요."))
        self.sex = input("성별을 입력하세요(남, 여).")
        self.position = input("직급을 입력하세요.")

comlist = list()
for i in range(0, 3):
    a=Company()
    comlist.append(a)

# print("")
# print("우리 회사의 조직도")
# # for num in range(0, 3):
# # print("이름: {} / 나이: {} / 성별: {} / 직급: {}".format(Company.name(), Company.age(), Company.sex(), Company.position()))
#
# # print(Company.name(1))
# print(Company.name[1])
