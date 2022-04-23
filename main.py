# This is a sample Python script.
# a, b = map(float, input().split())
from pathlib import Path
def print_hi():
    # a1, a2, a3, a4, a5, a6 = list(map(int, input().split()))
    # word_list = list(map(int, input().split()))
    #n = list(map(int,input()
    s=[]
    for i in range(0,11):
        s.append(i)
    print(*s)

    print(*range(11))
if __name__ == '__main__':
    print_hi()
