# Variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(type(print(my_string_variable,my_int_to_str_variable,my_bool_variable)))


# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name,surname,alias,age = "Brais", "Moure", 'MoureDev', 35
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

# Inputs

'''
first_name = input('¿Cuál es tu nombre?')
age = input('¿Qué edad tienes? ')

print(first_name)
print(age)
'''

# Cambiamos su tipo 
name = 35
age = "Brais"
print(name)
print(age)

