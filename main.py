# This is a sample Python script.
# a, b = map(float, input().split())
from pathlib import Path

# a1, a2, a3, a4, a5, a6 = list(map(int, input().split()))
# word_list = list(map(int, input().split()))
# n = list(map(int,input()
# word_list = list(map(int, input().split()))

def print_hi(word_list):

    rez = []

    for i in range(len(word_list)):

        rez.append(len(word_list[i]))

        #print(len(word_list[i]))
    return rez

if __name__ == '__main__':
    word_list = ["Москва", "Уфа", "Караганда", "Тверь", "Минск", "Казань"]
    print_hi(word_list)
