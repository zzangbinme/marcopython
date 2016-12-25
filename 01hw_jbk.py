# 맛집 고르기

meal = input("한식, 중식, 일식 중 하나를 고르시오")

list_kor=["수담", "토담골", "칠량", "애류헌", "목포집", "토말", "가온", "라연", "큰기와집"]
list_chn=["루안", "자금성", "현경", "대가방", "첸", "만리향", "운봉", "미래향", "연화루"]
list_jpn=["스시히로바","마코토", "호무랑", "미코", "미도", "아리아케", "키오쿠", "슌미", "기꾸스시"]

import random

if meal == "한식":
    a_1 = list_kor[random.randint(0,8)]
    print("한식당 {}를 추천합니다.".format(a_1))
elif meal == "중식":
    a_2 = list_chn[random.randint(0,8)]
    print("중식당 {}를 추천합니다.".format(a_2))
else:
    a_3 = list_jpn[random.randint(0,8)]
    print("일식당 {}를 추천합니다.".format(a_3))
