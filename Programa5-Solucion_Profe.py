arr = [0,0,0,0,0,0,0,0,0,0]  
# Lista de 10 elementos inicializados en 0 / List of 10 elements initialized to 0
car = []  
# Lista vacía para almacenar caracteres / Empty list to store characters
c = 0  
# Contador de posiciones para 'arr' / Counter for positions in 'arr'
c2 = 0  
# Contador de números válidos ingresados / Counter for valid numbers entered

while (True):
    a = input('Escribe un dato o valor: ')  
    # Pide un dato al usuario / Asks the user for a value
    if a.isdigit():
        arr[c] = int(a)  
        # Si es un número, lo guarda en 'arr' / If it's a number, store it in 'arr'
    elif a.isalpha():
        car.append(a)  
        # Si es texto, lo guarda en 'car' / If it's text, store it in 'car'
    c += 1  
    # Avanza el contador de posiciones / Increment position counter
    if c > 9:
        break  
        # Sale del ciclo cuando se llenan 10 posiciones / Exit loop when 10 positions are filled

print(f'La lista tiene {len(car)}')  
# Imprime cuántos elementos de texto se guardaron / Prints how many text elements were stored

for i in arr:
    if i != 0:
        c2 += 1  
        # Cuenta cuántos números se ingresaron realmente / Counts how many numbers were actually entered

print(f'El arreglo tiene {c2}')  
# Imprime la cantidad de números válidos / Prints the count of valid numbers
print(arr)  
# Muestra el contenido de 'arr' / Shows the content of 'arr'
