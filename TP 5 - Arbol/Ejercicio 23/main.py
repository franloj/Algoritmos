from tree import BinaryTree
from datos import criaturas_mitologicas

arbol_criaturas = BinaryTree()

for nombre, derrotador in criaturas_mitologicas:
    datos = {
        'derrotado_por': derrotador,
        'descripcion': '',
        'capturada': ''
    }
    arbol_criaturas.insert_node(nombre, datos)

print("--- Punto A: Listado inorden de criaturas y quienes las derrotaron ---")
def listar_inorden_criaturas(raiz):
    if raiz is not None:
        listar_inorden_criaturas(raiz.left)
        print(f"{raiz.value} - Derrotado por: {raiz.other_values['derrotado_por']}")
        listar_inorden_criaturas(raiz.right)

listar_inorden_criaturas(arbol_criaturas.root)
print()

print("--- Punto C: Información de Talos ---")
nodo_talos = arbol_criaturas.search("Talos")
if nodo_talos:
    print(f"Criatura: {nodo_talos.value}")
    print(f"Datos: {nodo_talos.other_values}")
print()

print("--- Punto D: Top 3 héroes/dioses que derrotaron más criaturas ---")
conteo_derrotas = {}

def contar_derrotas(raiz):
    if raiz is not None:
        contar_derrotas(raiz.left)
        heroe = raiz.other_values['derrotado_por']
        if heroe != '-':
            conteo_derrotas[heroe] = conteo_derrotas.get(heroe, 0) + 1
        contar_derrotas(raiz.right)

contar_derrotas(arbol_criaturas.root)

top_3_heroes = sorted(conteo_derrotas.items(), key=lambda x: x[1], reverse=True)[:3]
for heroe, cantidad in top_3_heroes:
    print(f"{heroe}: {cantidad} criaturas")
print()

print("--- Punto E: Criaturas derrotadas por Heracles ---")
def listar_por_heroe(raiz, heroe_buscado):
    if raiz is not None:
        listar_por_heroe(raiz.left, heroe_buscado)
        if raiz.other_values['derrotado_por'] == heroe_buscado:
            print(raiz.value)
        listar_por_heroe(raiz.right, heroe_buscado)

listar_por_heroe(arbol_criaturas.root, "Heracles")
print()

print("--- Punto F: Criaturas que no han sido derrotadas ---")
listar_por_heroe(arbol_criaturas.root, "-")
print()

print("--- Punto H: Actualizar criaturas capturadas por Heracles ---")
criaturas_a_capturar = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]
for nombre in criaturas_a_capturar:
    nodo = arbol_criaturas.search(nombre)
    if nodo:
        nodo.other_values['capturada'] = 'Heracles'
        print(f"{nombre} actualizado correctamente.")
print()

print("--- Punto I: Búsqueda por coincidencia ---")
termino = input("Ingrese una parte del nombre de la criatura para buscar: ")
arbol_criaturas.proxy_search(termino)
print()

print("--- Punto J: Eliminar al Basilisco y a las Sirenas ---")
arbol_criaturas.delete_node("Basilisco")
arbol_criaturas.delete_node("Sirenas")
print("Basilisco y Sirenas eliminados del árbol.")
print()

print("--- Punto K: Modificar Aves del Estínfalo ---")
nodo_aves = arbol_criaturas.search("Aves del Estínfalo")
if nodo_aves:
    nodo_aves.other_values['derrotado_por'] = 'Heracles derrotó a varias'
    print("Aves del Estínfalo modificado.")
print()

print("--- Punto L: Modificar el nombre de Ladón por Dragón Ladón ---")
nodo_ladon = arbol_criaturas.search("Ladón")
if nodo_ladon:
    datos_ladon = nodo_ladon.other_values
    arbol_criaturas.delete_node("Ladón")
    arbol_criaturas.insert_node("Dragón Ladón", datos_ladon)
    print("Ladón renombrado a Dragón Ladón.")
print()

print("--- Punto M: Listado por nivel del árbol ---")
arbol_criaturas.by_level()
print()

print("--- Punto N: Criaturas capturadas por Heracles ---")
def listar_capturadas_por(raiz, heroe_buscado):
    if raiz is not None:
        listar_capturadas_por(raiz.left, heroe_buscado)
        if raiz.other_values['capturada'] == heroe_buscado:
            print(raiz.value)
        listar_capturadas_por(raiz.right, heroe_buscado)

listar_capturadas_por(arbol_criaturas.root, "Heracles")