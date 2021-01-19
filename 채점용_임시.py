import os, re


def print_file(dir):

    files = os.listdir(dir)

    for item in files:
        print(item)
        file = open(dir + r"\\" + item, encoding="UTF-8").read()
        print(file)
        exec(open(dir + r"\\" + item, encoding="UTF-8").read())


if __name__ == "__main__":

    dir = r""  #path

    print_file(dir)
