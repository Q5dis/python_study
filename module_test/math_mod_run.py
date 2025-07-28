import math as m

print(m.factorial(5))

# 문제 1: 거리계산
x1, y1 = map(int, input("x1, y1: ").split())
x2, y2 = map(int, input("x2, y2: ").split())

dist = round(m.sqrt(m.pow(x2-x1, 2) + m.pow(y2-y1, 2)), 2)
print(f"거리: {dist}")

# 문제 2: 최대공배수와 최대공약수
teacher=24
students=18
print(f"""
학생선생 최대공약수/최소공배수
최대: {m.gcd(teacher,students)}
최소:  {m.lcm(teacher,students)}
""")