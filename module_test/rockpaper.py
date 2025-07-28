import random 

user=""
count=0
win_stack=0

rps=["가위","바위","보"]
s=0
r=0
p=0
while user!="X":
    computer=(random.choice(rps))
    user=input(">>> 가위,바위,보? enter X to exit: ")
    
    if user==computer:
        print("무승부")
        if user=="가위":
            s+=1
        elif user=="바위":
            r+=1
        else:
            p+=1
        count+=1
    else:
        if user=="가위":
            s+=1
            if computer=="보자기":
                print(f"{user}:{computer}, 승리!")
                win_stack+=1
                count+=1
            else:
                print(f"{user}:{computer}, 패배...")
                count+=1
        elif user=="바위":
            r+=1
            if computer=="가위":
                print(f"{user}:{computer}, 승리!")
                win_stack+=1
                count+=1
            else:
                print(f"{user}:{computer}, 패배...")
                count+=1
        elif user=="보":
            p+=1
            if computer=="바위":
                print(f"{user}:{computer}, 승리!")
                win_stack+=1
                count+=1
            else:
                print(f"{user}:{computer}, 패배...")
                count+=1

print(f"""
최종결과
가위바위보 실행 횟수: {count}
승리 횟수: {win_stack}

가위 낸 횟수: {s}
바위 낸 횟수: {r}
보 낸 횟수: {p}
""")