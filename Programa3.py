# Hacer un programa que lea 10 numeros y los almacene en un arreglo
# Program to read 10 numbers and store them in an array

a = [0,0,0,0,0,0,0,0,0,0]  
# Crea una lista de 10 elementos inicializados en 0 / Creates a list of 10 elements initialized to 0

for i in range(0,10):
<<<<<<< HEAD
    a[i] = int(input('Escribe un numero \n'))  
=======
    a[i] = int(input('Escribe un numero: '))  
>>>>>>> 7144771 (Tercera carga de elementos de mi parcial 1 info 3, con manual de practicas)
    # Pide un número al usuario y lo guarda en la posición i / Asks the user for a number and stores it at position i

for i in a:
    print(i)  
    # Imprime cada número almacenado en la lista / Prints each number stored in the list
