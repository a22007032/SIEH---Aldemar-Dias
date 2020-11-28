#!/usr/bin/python3
#coding=utf-8

import string
import random

def main():

	char = string.ascii_letters + string.punctuation + string.digits

	password_length = int(input("Quantos caracteres deve ter a Password (entre 8 e 32): "))

	if password_length < 8:
		print("Opção Invalida")
	elif password_length > 32:
		print("Opção Invalida")
	else:
		password =  ''.join(random.choice(char) for x in range(password_length))
		print(password)

if __name__ == "__main__":
	main()
