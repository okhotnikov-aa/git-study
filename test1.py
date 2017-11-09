# coding : utf-8

import os
import shutil


def pwd(folder):
    print(os.listdir(folder))


print("RUNNING")
print("1: copy")
print("2: delete")
print("q: exit")
answ1 = ""
folder = "/home/alex/Documents/PythonTest/"
while answ1 != "q":
    list = os.listdir(folder)
    i = 0
    answ1 = input()
    if answ1 == "q":
        break
    nmbr1 = int(answ1)
    print(answ1)
    if nmbr1 == 1:
        while i < len(list):
            newfile1 = list[i] + ".copy"
            shutil.copy(folder + list[i], folder + newfile1)
            i += 1
        pwd(folder)
    elif nmbr1 == 2:
        for l in list:
            if l.endswith(".copy"):
                os.remove(folder + l)
        pwd(folder)
