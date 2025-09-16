''' Hacer un programa que lea 10 datos, si el dato es un numero se almacenara en un arreglo
    si es un caracter o caracteres se metera a una lista, cuando finalice el programa, nos mostrara
    cuantos elementos numericos y caracteres '''
# Program to read 10 inputs, store numbers in an array and letters in a list, then show counts and sum
# Programa para leer 10 entradas, guardar números en un arreglo y letras en una lista, luego mostrar conteos y suma

lista = []  
# Lista vacía para almacenar letras / Empty list to store letters
arreglo = [0,0,0,0,0,0,0,0,0,0]  
# Arreglo de 10 elementos inicializados en 0 / Array of 10 elements initialized to 0
contadorIngresos = 0  
# Contador de datos ingresados / Counter for inputs entered
numeros = 0  
# Variable para contar números (no se usa en este código) / Variable to count numbers (not used in this code)
sumnum = 0  
# Variable para almacenar la suma de los números / Variable to store the sum of numbers

while contadorIngresos <= 9:
    dato = input('Ingresa un dato: ')  
    # Solicita un dato al usuario / Requests input from the user
    if dato.isdigit():
        contadorIngresos += 1  
        # Incrementa el contador si es número / Increments counter if input is a number
        arreglo.append(int(dato))  
        # Agrega el número al arreglo / Adds the number to the array
        sumnum = int(sumnum) + int(dato)  
        # Suma el número al total / Adds the number to the total sum
        print(sumnum)  
        # Muestra la suma parcial / Shows partial sum
    elif dato.isalpha():
        lista.append(dato)  
        # Si es letra, la agrega a la lista / If it's a letter, adds it to the list
<<<<<<< HEAD
        contadorIngresos += 1  
        #
=======
        contadorIngresos += 1
print(lista)
print(arreglo) 
>>>>>>> 7144771 (Tercera carga de elementos de mi parcial 1 info 3, con manual de practicas)
