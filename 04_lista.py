### Lista ### 

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30 ,30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Yensi Jesús", "González Nova"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])  # 35
print(my_other_list[1])  # 1.77
print(my_other_list[-1]) # González Nova
print(my_other_list[-2]) # Yensi Jesús
# print(my_other_list[4]) error
#print(my_other_list[-5]) error

age, height, name, surname = my_other_list
print(name)

#age, height, name, surname = my_other_list[2], my_other_list[1], my_other_list[0]
#print(age)

print (my_list + my_other_list)
#print (my_list - my_other_list)

my_other_list.append("Tapia")
print(my_other_list)

my_other_list.insert(1, "Negro")
print(my_other_list)

my_other_list.remove("Negro")
print(my_other_list)

my_list.remove(30)
print(my_list)

my_list.pop()
print(my_list)

my_list = "Hola Python"
print(my_list)
print(type(my_list))