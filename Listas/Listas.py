my_lista = ["rojo","azul","amarillo","naranja", "violeta", "verde"]
#input()
print(my_lista)
print(type(my_lista))
print(my_lista[2])
"""
print("my_lista size: ", len(my_lista))
print(my_lista[0:2])
print(my_lista[:2])

my_lista.append("blanco")  #Agrega elmeneto al final de la lista 
print(my_lista)

my_lista.insert(3, "negro")
print(my_lista)

my_lista.extend(["marron", "gris"])
print(my_lista)

print(my_lista.index("azul"))

#my_lista.remove("magenta")
my_lista.remove("marron")
print(my_lista)

my_lista.insert(8, "marron")
print(my_lista)

print(my_lista.pop())
size= len(my_lista)
print("size = ", size)
#print(my_lista.pop(size))

my_lista_3 = my_lista*3
print("my_lista_3: ", my_lista_3)

print("sort:")
print()
my_listasort = my_lista.sort()
print(my_listasort)

my_numList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]
print("Ordering my_numList: ")
my_numList.sort()
print(my_numList)
#OrderedLList = my_numList.sort()
#print(my_listaSort)

#ordenando lista de mayor a menor 
my_numList.sort(reverse = true)
print("de menor a mayor: ", my_numList) 

#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

#convertir una klista a una tupla:prin
print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")
my_tupla = tuple(my_lista)
print()
print()
print("my_tuple ",my_tupla)

print(my_tupla[o])
print(my_tupla[2])

#evaluar si un elmento esta contenido en la tupla(devuelve un valor booleano)
print("rojo" in my_tupla)
print(my_tupla.count("rojo"))

#tupla con un solo elemento
my_tupla_unitaria = ("blanco")
print(my_tupla_unitaria)

#empaquetado de tupla, tupla sin parentesis 
my_tupla = "gaspar", 5,8, 1999
print(my_tupla)

#desempaquetado de tupla, se guardan los cvalores en orden de las variables 
nombre, dia, mes, año =my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

print("nombre: ", nombre, "- dia:", dia, "-mes: ", mes, "-año: ", año)

#convertir una tupla en una lista 
my_lista2=list(my_tupla)
print(my_lista2)