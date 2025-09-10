# Declaraciones publicas o globales
# Public or global declarations
arr = [0,0,0,0,0,0,0,0,0,0]  
# Arreglo de 10 elementos inicializados en 0 / Array of 10 elements initialized to 0
car = []  
# Lista vacía para almacenar caracteres / Empty list to store characters

def resultados():  # Definicion para mostrar los resultados / Definition to show results
    c2 = 0  
    # Contador de números válidos / Counter for valid numbers
    print(f'La lista tiene {len(car)}')  
    # Muestra cantidad de elementos en la lista / Shows number of elements in the list
    for i in arr:
        if i != 0:
            c2 += 1  
            # Cuenta cuántos números válidos hay / Counts how many valid numbers there are
    print(f'El arreglo tiene {c2}')  
    # Muestra cantidad de números válidos en el arreglo / Shows count of valid numbers in array
    print(car)  
    # Muestra la lista de caracteres / Shows the list of characters
    print(arr)  
    # Muestra el arreglo de números / Shows the array of numbers

def hola():  # Definicion de metodo o funcion / Definition of method or function
    c = 0  
    # Contador de posiciones para el arreglo / Counter for positions in array
    while (True):
        a = input('Escribe un dato o valor: ')  
        # Pide un dato al usuario / Asks the user for a value
        if a.isdigit():
            arr[c] = int(a)  
            # Si es número, lo guarda en el arreglo / If it's a number, store it in the array
        elif a.isalpha():
            car.append(a)  
            # Si es texto, lo guarda en la lista / If it's text, store it in the list
        c += 1  
        # Incrementa el contador de posiciones / Increments the position counter
        if c > 9:
            break  
            # Sale del ciclo cuando se llenan 10 posiciones / Exits loop when 10 positions are filled
    resultados()  
    # Llama a la función para mostrar los resultados / Calls the function to show results

if __name__== "__main__":  # Metodo principal / Main method
    hola()  
    # Llama a la función principal / Calls the main function
