#!/usr/bin/python3
#coding=utf-8

x = ["windows", "macos", "solaris","android","ios"]

ficheiro = "exericio2.txt"
file = open(ficheiro,"w")

for item in x:
    if item != "solaris":
        print item
        file.write(item)



ficheiro = "exericio2.txt"
file = open(ficheiro,"w")

i = 0
while i < len(x):
    item = x
    if item != "solaris":
        print item
        file.write(item)

    i += 1

file.close()






