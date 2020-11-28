#!/usr/bin/python3
#coding=utf-8

import math

def lcm(n):  
    num = 1
    for i in range(1, 20):  
        num = int((num * i)/math.gcd(num, i))          
    return num
    
# main
num = 20
while num == num : 
    print (lcm(num))
    num -= 1 
    if num == 0:
        break
