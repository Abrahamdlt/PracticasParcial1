''' Hacer un programa que lea nombre, edad y sexo de 5 personas, estos elementos
tienen que estar dentro de una lista '''
# Program to read name, age, and gender of 5 people and store them in a list
# Programa para leer nombre, edad y sexo de 5 personas y guardarlos en una lista

# Declaraciones publicas
# Public declarations
lista = []  
# Lista vacía para almacenar los registros / Empty list to store records

def pedirDatos():  
    # Función para pedir los datos / Function to request data
    registros = 0  
    # Contador de personas ingresadas / Counter for entered people
    while registros <= 4:
        nombre = input('Ingresa un nombre: ')  
        # Solicita el nombre / Requests the name
        edad = input('Ingresa la edad: ')  
        # Solicita la edad / Requests the age
        sexo = input('Que sexo tiene [H] [M] : ')  
        # Solicita el sexo / Requests the gender
        lista.append(nombre+', '+edad+' años, sexo '+sexo)  
        # Agrega los datos concatenados a la lista / Adds the concatenated data to the list
        registros += 1  
        # Incrementa el contador / Increments the counter
    print(f'Registros: \n{lista}')  
    # Muestra todos los registros / Shows all records

pedirDatos()  
# Llama a la función para pedir datos / Calls the function to request data
