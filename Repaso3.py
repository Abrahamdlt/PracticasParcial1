''' Hacer un programa que lea un dato, el que sea, y que lo almacene en una lista, respetando su tipo de dato '''
# Program to read any input and store it in a list, keeping its data type
# Programa para leer cualquier dato y guardarlo en una lista respetando su tipo

lista = []  
# Lista vacía para almacenar los datos / Empty list to store inputs

def validar(a):  
    # Función para determinar el tipo de dato / Function to determine the data type
    ne = 0  
    # Variable auxiliar para enteros / Auxiliary variable for integers
    nf = 0.0  
    # Variable auxiliar para flotantes / Auxiliary variable for floats

    try:
        ne = int(a)  
        # Intenta convertir a entero / Tries to convert to integer
        return ne  
        # Devuelve el entero / Returns the integer
    except ValueError:
        print('No es un entero')  
        # Mensaje si no es entero / Message if not integer

    try:
        nf = float(a)  
        # Intenta convertir a float / Tries to convert to float
        return nf  
        # Devuelve el float / Returns the float
    except ValueError:
        print('No es un entero con decimales')  
        # Mensaje si no es float / Message if not float

    return(a)  
    # Si no es número, devuelve el valor original / If not a number, returns original input

def leer():  
    # Función para leer un dato y almacenarlo / Function to read input and store it
    a = input('Escribe un dato: ')  
    # Solicita un dato al usuario / Requests input from user
    dato = validar(a)  
    # Valida el tipo de dato / Validates data type
    lista.append(dato)  
    # Agrega el dato a la lista / Appends the data to the list

if __name__== '__main__':  
    # Punto de entrada principal / Main entry point
    while(True):
        leer()  
        # Llama a la función leer / Calls the read function
        res = input('Deseas otro s/n: ')  
        # Pregunta si desea ingresar otro dato / Asks if user wants to enter another input
        if res == 'n' or res == 'N':  
            print(lista)  
            # Muestra la lista final / Displays the final list
            break  
            # Sale del ciclo / Exits the loop