a = [10]  # Lista con un elemento / List with one element
b = []  # Lista vacía / Empty list

a[0] = 10  # Asigna 10 al primer elemento / Assigns 10 to the first element
a[0] = 10  # Repite la asignación (redundante) / Repeats the assignment (redundant)

b = {'Hola', 10, 10.05, False, 'm', {1, 2, 3, 4}}  
# Set con varios tipos (error: un set no puede estar dentro de otro) 
# Set with multiple types (error: a set cannot contain another set)

# Ciclos y condiciones / Loops and conditions
if (len(a) > len(b)):
    print('A es mayor')  # Imprime si 'a' es más grande / Prints if 'a' is larger
else:
    print('B es mayor')  # Imprime si 'b' es más grande / Prints if 'b' is larger

for i in a:
    print(a)  # Imprime toda la lista en cada iteración / Prints the whole list each iteration
