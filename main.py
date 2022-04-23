# This is a sample Python script.
# a, b = map(float, input().split())
from pathlib import Path
def print_hi():
    # a1, a2, a3, a4, a5, a6 = list(map(int, input().split()))
    # word_list = list(map(int, input().split()))
    #n = list(map(int,input()
    lst_in = ['Муму', 'Евгений Онегин', 'Сияние', 'Мастер и Маргарита', 'Пиковая дама', 'Колобок']
    i = 0
    rez = []
    while i < len(lst_in):
        if len(lst_in[i].split(" ")) < 2:
            rez.append(lst_in[i])
            rez.append("\n")
        i +=1

    joined_string = "".join(rez)
    print(joined_string)

if __name__ == '__main__':
    print_hi()
