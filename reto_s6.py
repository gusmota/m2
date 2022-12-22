# pedimos al usuario una contrasena

while True:
    password = input("Introduce la contraseña empezando con un número: ")
    if password[0].isnumeric():
        break
    else:
        print("La contraseña debe empezar con un número")

# ingrese nuevamamente
for i in range(3):
    password_2 = input("Introduce la contraseña nuevamente: ")
    if password == password_2:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta")

print("Fin del programa")