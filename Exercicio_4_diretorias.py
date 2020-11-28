#!/usr/bin/python3
#coding=utf-8

#nome_diretoria = input("Indicar nome da diretoria: ")
#novo_nome_diretoria = input("Indicar novo nome para a diretoria: ")

#Objetivo:  Criar um programa que permite criar(os.mkdir), renomear(os.rename), remover(os.remove) e listar diretorias(os.dir)
import os
import sys

def criar_diretorias():
    "permite criar uma nova diretoria"
    nome_diretoria = input("Indicar nome da diretoria: ")
    os.mkdir(str(nome_diretoria))

def renomear_diretorias():
    "permite dar um novo nome a uma diretoria"
    nome_diretoria = input("Indicar nome da diretoria: ")
    novo_nome_diretoria = input("Indicar novo nome para a diretoria: ")
    os.rename(str(nome_diretoria), str(novo_nome_diretoria))

def remover_diretorias():
    "permite remover uma diretoria"
    nome_diretoria = input("Indicar nome da diretoria: ")
    os.rmdir(str(nome_diretoria))

def listar_diretorias():
    "permite listar todas as diretorias"
    os.dir()

def main():
    action = input("Escolher ação: ")
    if action == "" :
        print("deve escolher opção")
    elif action == "listar":
        listar_diretorias()
    elif action == "criar":
        criar_diretorias()		
    elif action == "renomear":
        renomear_diretorias()
    elif option == "remover":
        remover_diretorias()
    else:
        print("Wrong option!\n")		

if __name__ == "__main__":
	main()
