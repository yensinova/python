### SETS ### 

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # inicialmente es un diccionario

my_other_set = {"Yensi", "Nova", 22}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("González")

print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("González") # Un set no admite repetidos

print(my_other_set) 

print("Nova" in my_other_set)
print("Jesús" in my_other_set)

my_other_set.remove("Nova")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

my_set = {"Yensi","Nova",22}
my_list = list(my_set)
print(my_list)