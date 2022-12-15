# pedir al usuario que ingrese el año actual y otro año

try:
    current_year = int(input("Ingrese el año actual: "))
    other_year = int(input("Ingrese otro año: "))

except:
    print('Ingrese un valor numérico')

# si el año es menor, cuántos han pasado
if current_year > other_year:
    print(f'Han pasado {other_year - current_year} años')

# si el año es mayor, cuántos faltan
elif current_year < other_year:
    print(f'Faltan {other_year - current_year} años')

# si el año es igual, decir que es el mismo año
else:
    print('Es el mismo año')
