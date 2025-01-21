"""Generar una contraseña que contenga una palabra, un caracter especial y un numero"""
import random

palabras = ["hola", "hoy", "ayer", "chin", "chan", "dia", "mañana", "prueba", "pelota"]
caracteres = ["!", "@", "/", "&", "%", "$", ".", "-", "+", "-", "*", "?", "¿", "=",")", "(", ")"]
totalp = len(palabras) - 1
totalc = len(caracteres) - 1

count = 0
archivo = open("text.txt", "w")
while count <= 11:
    archivo.write(palabras[random.randint(0, totalp)] + caracteres[random.randint(0, totalc)] + palabras[random.randint(0, totalp)] + str(random.randint(0, 101)))
    archivo.write("\n")
    count = count + 1
archivo.close()

