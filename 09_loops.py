### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2

if my_condition == 10:
    print("Mi condición es igual a 10")
else:
    print("Mi condición es mayor o igual a 10")

# FOR

my_list = [35, 24, 62, 52, 30, 31, 17]

for element in my_list: 
    print(element)

my_tuple = (35, 1.85, "Yensi Jesús", "González", "Nova")

for element in my_tuple: 
    print(element)

my_set = {"Yensi", "Nova", 22}

for element in my_set: 
    print(element)

my_dict = {"Nombre":"Yensi", "Apellido":"Nova", "Edad":22}

for element in my_dict: 
    print(element)
    if element == "Edad":
        break
    print("Se ejecuta el break")
else: 
    print("El bucle for para diccionario ha finalizado")