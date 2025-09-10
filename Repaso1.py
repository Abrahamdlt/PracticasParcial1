# # Instrucciones de entrada y salida
# # print() o print(f)
# print('Hola mundo')
# print(f'Hola mundo numeros {10}')

# # Entrada de datos
# input ('Escribe un numero: ') # Se introducen solo letras

# # Casting para convertir a valores especificos
# f = 0.0
# f = float(input('Escribe un numero con decimales: '))
# a = 0
# a = int(input('Escribe un numero: '))
# c = 120
# print(str(c))
# v = ''
# v = str(c)
# # NOTA: Solo las variables que no se introducen por teclado se obliga a inicializarlas.

''' Hacer un programa que lea nombre y precio de un producto, el programa calculara
el costo y precio de venta, el costo involucra el # # Instrucciones de entrada y salida
# # print() o print(f)
# print('Hola mundo')  
# Muestra un mensaje en pantalla / Displays a message on screen
# print(f'Hola mundo numeros {10}')  
# Muestra un mensaje con un número usando f-string / Displays a message with a number using f-string

# # Entrada de datos
# input('Escribe un numero: ')  
# Solicita al usuario un dato (cadena) / Requests input from the user (string)

# # Casting para convertir a valores especificos
# f = 0.0  
# Inicializa una variable flotante / Initializes a float variable
# f = float(input('Escribe un numero con decimales: '))  
# Convierte la entrada a float / Converts input to float
# a = 0  
# Inicializa una variable entera / Initializes an integer variable
# a = int(input('Escribe un numero: '))  
# Convierte la entrada a entero / Converts input to integer
# c = 120
# print(str(c))  
# Convierte un entero a cadena / Converts an integer to string
# v = ''  
# v = str(c)  
# Otra forma de convertir entero a cadena / Another way to convert integer to string
# NOTA: Solo las variables que no se introducen por teclado se obliga a inicializarlas.  
# NOTE: Only variables not input from keyboard need to be initialized

Hacer un programa que lea nombre y precio de un producto, el programa calculara
el costo y precio de venta, el costo involucra el 12% y el iva 16% 
# Program to read product name and price, calculate cost with 12% and selling price with 16% VAT
# Programa para leer nombre y precio de un producto, calcular costo con 12% y precio de venta con 16% IVA

# while(True):
for i in range(0,5):
    # Ciclo para procesar 5 productos / Loop to process 5 products
    nombre = input('Escribe el nombre de un prducto: ')  
    # Solicita nombre del producto / Requests product name
    precio = float(input('Escribe el precio de el producto: '))  
    # Solicita precio y lo convierte a float / Requests price and converts to float
    preciofloatc = float(precio * 1.12)  
    # Calcula el costo con 12% / Calculates cost with 12%
    preciofloativa = preciofloatc * 1.16  
    # Calcula el precio de venta con 16% IVA / Calculates selling price with 16% VAT
    print(f'El costo es: {preciofloatc:.2f}')  
    # Muestra el costo con 2 decimales / Displays cost with 2 decimals
    print(f'El precio de venta es: {preciofloativa:.2f}')  
    # Muestra el precio de venta con 2 decimales / Displays selling price with 2 decimals
    res = input('Deseas otro numero? s/n: ')  
    # Pregunta si desea ingresar otro producto / Asks if the user wants to enter another product
    if res == 'n' or 'N':  
        break  
        # Sale del ciclo si la respuesta es 'n' / Exits loop if answer is 'n'

# :.2f es para que al mostrar el flotante solo muestre 2 decimales
# :.2f is used to display floats with only 2 decimal places
12% y el iva 16% '''

# while(True):
for i in range(0,5):
    nombre = input('Escribe el nombre de un prducto: ')
    precio = float(input('Escribe el precio de el producto: '))
    preciofloatc = float(precio * 1.12)
    preciofloativa = preciofloatc * 1.16
    print(f'El costo es: {preciofloatc:.2f}')
    print(f'El precio de venta es: {preciofloativa:.2f}')
    res = input('Deseas otro numero? s/n: ')
    if res == 'n' or 'N':
        break

# :.2f es para que al mostrar el flotante solo muestre 2 decimales