#para crear mas de un numero random usando la funcion random tienes que usar un for con la cantidad de iteraciones y eso, entonces dependiendo del numero que ingrese al usuario lo ponemos en el for y le damos con el random
import random

letras_minusculas = int(input("minusculas: "))
letras_mayusculas = int(input("mayusculas: "))
simbolos_usuario =  int(input("simbolos: "))
numeros_usuario = int(input("numeros: "))

# Cadena de caracteres
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnopqrstuvwxyz"
simbolos = "!@#$%^&*()_-+=[]{}\|;:',<,>.?/¡¿"
numeros = "0123456789"

caracter_min = random.sample(minusculas, letras_minusculas)
caracter_max = random.sample(mayusculas, letras_mayusculas)
caracter_simb = random.sample(simbolos, simbolos_usuario)
caracter_num = random.sample(numeros, numeros_usuario)

#ahora tengo que juntar todos los caracter_ y crear la password
concatenada = caracter_min+caracter_max+caracter_simb+caracter_num #esto es una lista
random.shuffle(concatenada)
separador = ""
cadena = separador.join(concatenada)

print("contraseña:",cadena)