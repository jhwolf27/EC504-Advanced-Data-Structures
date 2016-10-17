# AUTHOR: Jackson Hsu jaxhsu@bu.edu

import math, re, string




def most_common(lst):
    return max(lst, key=lst.count)

def Analyze(str, size):
    list = []
    strlen = len(str)
    quotes = '"'

    for i in range(0, strlen):
        list.append(str[i:(size+i)])
    listlen = len(list)
    mode = most_common(list)

    if (size >= strlen):
        print(quotes + str + quotes)
    else:
        print(quotes + mode + quotes)

def main():
    str = input("Input str: ")
    sizstr = input("Input size of str: ")
    size = int(sizstr)
    Analyze(str, size)

main()