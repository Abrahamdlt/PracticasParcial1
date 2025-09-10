# Hacer un programa que lea una cadena y muestre en pantalla cuantos
# numeros tiene, cuantas mayusculas, cuantas minusculas y cuantos espacios
# Program to read a string and display the count of numbers, uppercase, lowercase, and spaces

def inicio():  
    # Función principal / Main function
    mi = 0  
    # Contador de letras minúsculas / Lowercase letters counter
    may = 0  
    # Contador de letras mayúsculas / Uppercase letters counter
    c = 0  
    # Contador de números / Numbers counter
    e = 0  
    # Contador de espacios / Spaces counter
    numeros = "1234567890"  
    # Cadena con dígitos para validar números / String with digits to check numbers
    cadena = input('Escribe una cadena: ')  
    # Solicita al usuario una cadena / Requests a string from the user

    for i in cadena:
        if i in numeros:
            c += 1  
            # Incrementa el contador de números / Increments the numbers counter
        if i == ' ':
            e += 1  
            # Incrementa el contador de espacios / Increments the spaces counter
        if ord(i) >= 97 and ord(i) <= 122:
            mi += 1  
            # Incrementa el contador de minúsculas / Increments the lowercase counter
        if ord(i) >= 65 and ord(i) <= 90:
            may += 1  
            # Incrementa el contador de mayúsculas / Increments the uppercase counter

    print(f'\nLos numeros son: {c}\ny los espacios: {e}\ny las minusculas: {mi}\ny las mayusculas: {may}\n')  
    # Muestra los resultados / Displays the results

if __name__== '__main__':
    inicio()  
    # Llama a la función principal / Calls the main function
