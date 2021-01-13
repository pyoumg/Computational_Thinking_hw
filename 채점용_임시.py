import os, re


def print_file(dir):

    files = os.listdir(dir)

    for item in files:
        print(item)
        file = open(dir + r"\\" + item, encoding="UTF-8").read()
        print(file)
        exec(open(dir + r"\\" + item, encoding="UTF-8").read())


if __name__ == "__main__":

    dir = r"C:\Users\alluo\Downloads\[2020-겨울학기-컴퓨팅사고력-01]Ch8과제"

    print_file(dir)
