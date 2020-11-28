#!/usr/bin/python3.7
#coding=utf-8

#    • Exercício 1:
#Criar um programa para converter um valor em segundos em horas, minutos e segundos
#Requisitos Exercício 1:
#O programa deve pedir os segundos ao utilizador e guardar em uma variável
#De seguida o programa deverá calcular o total de horas, minutos e segundos e imprimir o resultado na consola
#Exemplo Exercício 1:
#39050 segundos é igual a 10:50:50

seconds = float(input("Insert time in seconds: "))
hour = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
seconds1 = seconds

print(str(seconds) + " segundos é igual a %d:%d:%d" % (hour, minutes, seconds1))
