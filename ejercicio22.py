# 22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
# ayuda de la fuerza” realizar las siguientes actividades:

# a.sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
# queden más objetos en la mochila;

# b.determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
# car para encontrarlo;

# c.Utilizar un vector para representar la mochila.

def usar_la_fuerza(mochila: list, objetos_sacados: int = 0):
    if len(mochila) == 0:
        return False, objetos_sacados
    elif mochila[0] == "sable de luz":
        return True, objetos_sacados + 1
    else:
        return usar_la_fuerza(mochila[1:], objetos_sacados + 1)


mochila_1 = ["comunicador", "capa", "sable de luz", "botiquín", "comida"]
encontrado_1, sacados_1 = usar_la_fuerza(mochila_1)

print("--- PRUEBA 1 ---")
if encontrado_1:
    print(f"¡Sable encontrado! El Jedi sacó {sacados_1} objetos.")
else:
    print(f"No hay sable. El Jedi revisó {sacados_1} objetos en vano.")


mochila_2 = ["raciones", "capa", "botiquín", "binoculares", "mapa"]
encontrado_2, sacados_2 = usar_la_fuerza(mochila_2)

print("--- PRUEBA 2 ---")
if encontrado_2:
    print(f"¡Sable encontrado! El Jedi sacó {sacados_2} objetos.")
else:
    print(f"No hay sable. El Jedi revisó {sacados_2} objetos en vano.")