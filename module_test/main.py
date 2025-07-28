# 파이썬 표준 라이브러리

# 수학연산 모듈
import math
print("math 모듈-----")
# 1. 올/내림 
print("올,내림",round(3.141592, 2))

# 소수점 지정 없는...
# 올림
print("올림",math.ceil(3.14))
# 내림
print("내림",math.floor(3.14))

# 2. 제곱, 제곱근

# pow(x,y): 제곱-x^y를 반환
print("제곱 반환",math.pow(2,3))
# sqrt(x): 제곱근 반환
print("제곱근 반환",math.sqrt(16))

# 3. 상수
print("상수",math.pi)

# 4. 수학 계산 편의기능
print("팩토리얼",math.factorial(5))
print("최대공약수",math.gcd(12,20))
print("최소공배수",math.lcm(10,20))



# 랜덤모듈
import random
print("\n랜덤모듈-------")
# seed(a) 최초 생성 난수 고정 시 사용
random.seed(40)

# 0이상 1미만 난수반환
print("0이상 1미만 난수반환",random.random())

# uniform(a,b) a이상 b이하 실수난수 반환
print("a이상 b이하 실수난수 반환",random.uniform(1,10))

# ranint(a,b) a이상 b이하의 정수난수 반환
print("a이상 b이하의 정수난수 반환",random.randint(1,100))

# randrange(start, stop, step) 간격지정가능한 난수반환
print("간격지정가능한 난수반환",random.randrange(0,100,5))

# 랜덤선택
fruit=["apple","grape","watermelon"]

# 한개만
print("한개만",random.choice(fruit))
# k개 만큼
print("k개 만큼",random.choices(fruit, k=2))
# k개 만큼, 다만 중복없음
print("k개 만큼, 중복불가",random.sample(fruit,k=2))
# 원본 시퀀스를 변경, 섞어버린다
print("원본 리스트:",fruit)
random.shuffle(fruit)
print("변경된 리스트:",fruit)



# datetime 모듈: 날짜 시간 생성 조작 현실변환 같은 시간관련 기능 제공

import datetime as d
print("\ndatetime 모듈----")
print("날짜와 시간",d.datetime.now())
now=d.datetime.now()
print("오늘 날짜만",d.date.today())
today=d.date.today()
# 날짜와 시간의 형변환
formatted=now.strftime("%Y/%m/%d %H:%M:%S") # 연 월 일 시 분 초 
print(formatted)


parsed=d.datetime.strptime(formatted, "%Y/%m/%d %H:%M:%S") # 포맷 풀기
print(type(parsed))

#날짜 시간 연산
dt= d.date(2025,7,7)
passed=today-dt
print(f"현재 개강일부터 {passed.days}일 경과")

# 요일반환
print(today.weekday()) # 0월~7일요일
weeks=["월","화","수","목","금","토","일"]
print(f"오늘은 {weeks[today.weekday()]}요일")

# 캘린더 모듈
import calendar
print("캘린더 출력")
print(calendar.prmonth(8001,4))