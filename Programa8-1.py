# El programa no termina hasta que la lista tenga 5 elementos
# The program doesn't end until the list has 5 elements

lista = []  
# Lista vacía para almacenar cadenas válidas / Empty list to store valid strings

def inicio():  
    # Función para ingresar y validar cadenas / Function to input and validate strings
    numeros = "1234567890"  
    # Cadena con dígitos para validación / String with digits for validation
    elementos = 0  
    # Contador de cadenas válidas ingresadas / Counter for valid strings entered
    error = 0  
    # Contador de errores de validación / Counter for validation errors

    while elementos <= 4:
        cadena = input('Escribe algo: ')  
        # Solicita la cadena al usuario / Requests a string from the user

        for i in cadena:
            if i in numeros:
                print('No deve haber numeros\n')  
                # Mensaje si hay números / Message if numbers exist
                error += 1
                break

        for i in cadena:
            if i == ' ':
                print('No deve haber espacios\n')  
                # Mensaje si hay espacios / Message if spaces exist
                error += 1
                break

        if ord(cadena[0])>=97 and ord(cadena[0])<=122:
            print('La primer letra deve ser mayuscula\n')  
            # Verifica que la primera letra sea mayúscula / Checks if first letter is uppercase
            error += 1

        for i in cadena[1:]:
            if ord(i)>=65 and ord(i)<=90:
                print('Solo la primer letra deve ser mayuscula\n')  
                # Solo la primera letra puede ser mayúscula / Only the first letter can be uppercase
                error += 1
                break

        for i in cadena:
            ba = False
            be = False
            bi = False
            bo = False
            bu = False
            # Variables para verificar cada vocal / Variables to check each vowel
            if 'a' in cadena or 'A' in cadena:
                ba = True
            if 'e' in cadena or 'E' in cadena:
                be = True
            if 'i' in cadena or 'I' in cadena:
                bi = True
            if 'o' in cadena or 'O' in cadena:
                bo = True
            if 'u' in cadena or 'U' in cadena:
                bu = True
            if ba == True and be == True and bi == True and bo == True and bu == True and int(error) == 0:
                # Si tiene todas las vocales y no hay errores / If all vowels are present and no errors
                elementos += 1  
                lista.append(cadena)  
                error = 0
                break
            else:
                print('No tiene todas las vocales')  
                # Mensaje si faltan vocales / Message if vowels are missing
                error = 0
                break

if __name__=='__main__':
    while(True):
        inicio()  
        # Llama a la función de entrada / Calls the input function
        if len(lista) >= 5:
            print(lista)  
            # Imprime la lista final cuando tenga 5 elementos / Prints the final list when it has 5 elements
            break
