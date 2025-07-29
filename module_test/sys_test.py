import sys


args=sys.argv
print(args)

# 실행하고 경로에서 python sys_test.py dog cat 시, 
# ['sys_test.py', 'dog', 'cat'] 하고 프린트됨?

total =0
for i in args:
    total+=int(i)
