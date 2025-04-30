#print("hola a todos ")
# estructura de datos dinamicas 
# Listas
# Tuplas
# Conjuntos 
# Diccionarios 

'''
nombres = ["Alberto","Alejandro","Alejandro","Angel","Alicia","Brayan","Carla"]
for x in nombres:
    print(x)
'''
print("================= Antes de la Ejecucion  =================")

datos = [15,13.9,True,False,"Maria del Rosario",14,15,13.9,True,False,"Maria del Rosario",14,15,13.9,True,False,"Maria del Rosario",14,15,13.9,True,False,"Maria del Rosario",14,"oso polar"]

# print(datos[1])

# print(datos[4])

print("=======================================")

cantidadElementos = len(datos)

print("la cantidad nueva es: ", cantidadElementos)

#dato = datos[cantidadElementos-1]

print("=======================================")

datos.remove("Maria del Rosario")

cantidadElementosNuevos = len(datos)

print("la cantidad nueva es: ", cantidadElementosNuevos)

# datos.insert(5+30,"Francisco")
# #datos.append("Francisco")

# for y in datos:
#     print(y)



datostupla = (15,13.9,True,False,"Maria del Rosario",14)
datostupla.append("Francisco")
print("hola a todos esto es un cambio")


print("hola mundo")








