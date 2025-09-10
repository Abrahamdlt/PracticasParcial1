a = 1
b = 2
c = -15
# Variables del trinomio ax^2 + bx + c / Variables of the trinomial ax^2 + bx + c

p = 0
m = 0
r = 0
ra = 0.0
d = 0.0
x1 = 0.0
x2 = 0.0
# Variables auxiliares para cálculo / Auxiliary variables for calculation

p = b**2  
# Calcula b al cuadrado / Calculates b squared
m = 4*a*c  
# Calcula 4*a*c / Calculates 4*a*c
r = p - m  
# Calcula el discriminante / Calculates the discriminant

if r > 0:
    print('Si se puede')  
    # Si el discriminante es positivo, hay soluciones reales / If discriminant is positive, real solutions exist
    ra = r ** (1/2)  
    # Calcula la raíz cuadrada del discriminante / Calculates square root of discriminant
    d = 2 * a  
    # Calcula el denominador de la fórmula / Calculates denominator of formula
    x1 = (-b + ra) / d  
    # Calcula la primera raíz / Calculates first root
    x2 = (-b - ra) / d  
    # Calcula la segunda raíz / Calculates second root
    print(f'El valor de x1 es: {x1:.2f}, Y el de x2: {x2:.2f}')  
    # Muestra los valores de x1 y x2 con 2 decimales / Displays x1 and x2 values with 2 decimals
else:
    print('No se puede')  
    # Si el discriminante es negativo, no hay soluciones reales / If discriminant is negative, no real solutions
