import json
from tree import BinaryTree

with open('datos.json', 'r', encoding='utf-8') as archivo:
    pokemons = json.load(archivo)

arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

for poke in pokemons:
    arbol_nombre.insert_node(poke["nombre"], poke)
    arbol_numero.insert_node(poke["numero"], poke)
    for tipo in poke["tipos"]:
        arbol_tipo.insert_node(tipo, poke)

print("--- 1. Búsqueda exacta por número ---")
try:
    num_buscado = int(input("Ingrese el número del Pokémon que desea buscar (ej: 25): "))
    resultado_numero = arbol_numero.search(num_buscado)
    if resultado_numero:
        print(f"Encontrado: {resultado_numero.other_values}")
    else:
        print("No se encontró ningún Pokémon con ese número.")
except ValueError:
    print("Error: Debe ingresar un valor numérico.")

print("\n--- 2 y 3. Búsqueda por proximidad y ficha completa ---")
prox_buscado = input("Ingrese una parte del nombre a buscar (ej: 'bul' o 'Venusaur'): ").strip().lower()
print(f"Resultados para '{prox_buscado}':")
arbol_nombre.proxy_search(prox_buscado)

print("")
nom_buscado = input("¿Querés ver los datos completos de alguno? Ingresá el nombre exacto (o presioná Enter para seguir): ").strip().capitalize()

if nom_buscado:
    resultado_nombre = arbol_nombre.search(nom_buscado)
    if resultado_nombre:
        print(f"Encontrado: {resultado_nombre.other_values}")
    else:
        print("No se encontró ningún Pokémon con ese nombre exacto.")


print("\n--- 4. Pokémons de tipo Fantasma, Fuego, Acero y Eléctrico ---")
def mostrar_por_tipos(root, tipos_buscados):
    if root is not None:
        mostrar_por_tipos(root.left, tipos_buscados)
        if root.value in tipos_buscados:
            print(f"Tipo {root.value}: {root.other_values['nombre']}")
        mostrar_por_tipos(root.right, tipos_buscados)

mostrar_por_tipos(arbol_tipo.root, ["Fantasma", "Fuego", "Acero", "Eléctrico"])


print("\n--- 5. Listado ascendente por número ---")
def inorden_info(root):
    if root is not None:
        inorden_info(root.left)
        print(f"N° {root.value} - {root.other_values['nombre']}")
        inorden_info(root.right)

inorden_info(arbol_numero.root)


print("\n--- 6. Listado ascendente por nombre ---")
def inorden_nombres(root):
    if root is not None:
        inorden_nombres(root.left)
        print(f"{root.value} (N° {root.other_values['numero']})")
        inorden_nombres(root.right)

inorden_nombres(arbol_nombre.root)


print("\n--- 7. Listado por nivel por nombre ---")
arbol_nombre.by_level()


print("\n--- 8. Pokémons débiles frente a Jolteon (Eléctrico), Lycanroc (Roca) y Tyrantrum (Roca/Dragón) ---")
def buscar_debilidades(root):
    if root is not None:
        buscar_debilidades(root.left)
        
        atacantes = []
        if "Eléctrico" in root.other_values["debilidades"]:
            atacantes.append("Jolteon (Eléctrico)")
        if "Roca" in root.other_values["debilidades"]:
            atacantes.append("Lycanroc/Tyrantrum (Roca)")
        if "Dragón" in root.other_values["debilidades"]:
            atacantes.append("Tyrantrum (Dragón)")

        if atacantes:
            print(f"{root.value} es débil frente a: {', '.join(atacantes)}")
            
        buscar_debilidades(root.right)

buscar_debilidades(arbol_nombre.root)


print("\n--- 9. Tipos de Pokémons y cuántos hay de cada uno ---")
def contar_tipos(root, diccionario_tipos):
    if root is not None:
        contar_tipos(root.left, diccionario_tipos)
        tipo = root.value
        if tipo in diccionario_tipos:
            diccionario_tipos[tipo] += 1
        else:
            diccionario_tipos[tipo] = 1
        contar_tipos(root.right, diccionario_tipos)

conteo = {}
contar_tipos(arbol_tipo.root, conteo)
for tipo, cantidad in conteo.items():
    print(f"Tipo {tipo}: {cantidad} Pokémons")


print("\n--- 10. Cantidad de Pokémons con Megaevolución y Gigamax ---")
def contar_mega_giga(root, contadores):
    if root is not None:
        contar_mega_giga(root.left, contadores)
        if root.other_values["mega"]:
            contadores["mega"] += 1
        if root.other_values["gigamax"]:
            contadores["gigamax"] += 1
        contar_mega_giga(root.right, contadores)

contadores = {"mega": 0, "gigamax": 0}
contar_mega_giga(arbol_nombre.root, contadores)
print(f"Con Megaevolución: {contadores['mega']}")
print(f"Con forma Gigamax: {contadores['gigamax']}")