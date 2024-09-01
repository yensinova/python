### DICCIONARIOS ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {
    "Nombre": "Yensi Jesús",
    "Apellidos": "González Nova",
    "Edad": 22,
    1: "Python",
}

my_dict = {
    "Nombre": "Yensi Jesús",
    "Apellidos": "González Nova",
    "Edad": 22,
    "Lenguajes": {"Python", "Swift", "PHP"},
    1: 1.85,
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle Pasaje de Chiloeches 20"

print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Yensi" in my_dict)
print("Apellidos" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
'''
my_list = ["Nombre", 1, "`Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys((my_dict, 1, "Yensi"))
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

'''