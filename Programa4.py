'''Hacer un programa que lea 10 numeros y los almacene en una lista'''
# Program to read 10 numbers and store them in a list

a = []  
# Lista vacía para almacenar los números / Empty list to store the numbers
s = 0  
# Variable para la suma de los números / Variable for the sum of numbers
n = 0  
# Contador de números válidos ingresados / Counter for valid numbers entered
numeros = "0123456789"  
# Cadena con dígitos para validar la entrada / String with digits to validate input

while (n < 10):
    b = input('Escribe un numero: ')  
    # Pide un número al usuario / Asks the user for a number
    x = 0  
    # Contador de caracteres válidos / Counter for valid characters
    for i in b:
        if i in numeros:
            x += 1  
            # Incrementa x si el caracter es un dígito / Increments x if the character is a digit
    if len(b) == x:
        a.append(int(b))  
        # Convierte a entero y agrega a la lista / Converts to integer and appends to the list
        n += 1  
        # Incrementa el contador de números válidos / Increments the counter of valid numbers
    else:
        print('El valor no es numero.')  
        # Mensaje si la entrada no es válida / Message if input is not valid

for i in a:
    print(i)  
    # Imprime cada número de la lista / Prints each number in the list
    s += i  
    # Suma los números / Adds the numbers
print(f'La suma es: {s}')  
# Imprime la suma total / Prints the total sum
