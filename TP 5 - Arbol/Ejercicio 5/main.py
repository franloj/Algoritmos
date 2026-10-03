from tree import BinaryTree
from datos_mcu import personajes_marvel

arbol_mcu = BinaryTree()

for nombre, es_heroe in personajes_marvel:
    arbol_mcu.insert_node(nombre, {'is_villain': not es_heroe})

print("--- Punto B: Villanos ordenados alfabéticamente ---")
arbol_mcu.inorden_villain()
print()

print("--- Punto C: Superhéroes que empiezan con C ---")
arbol_mcu.inorden_hero_star_with('C')
print()

print("--- Punto D: Cantidad de superhéroes ---")
total_heroes = arbol_mcu.count_heroes()
print(f"Hay {total_heroes} superhéroes en el árbol.")
print()

print("--- Punto E: Corregir Doctor Strange por proximidad ---")
def corregir_por_proximidad(arbol, buscado, nombre_correcto):
    def _buscar(raiz, texto):
        if raiz is not None:
            if texto.lower() in raiz.value.lower():
                return raiz
            izq = _buscar(raiz.left, texto)
            if izq:
                return izq
            return _buscar(raiz.right, texto)
        return None

    nodo_error = _buscar(arbol.root, buscado)
    if nodo_error:
        datos = nodo_error.other_values
        print(f"Se encontro '{nodo_error.value}', corrigiendo a '{nombre_correcto}'...")
        arbol.delete_node(nodo_error.value)
        arbol.insert_node(nombre_correcto, datos)

corregir_por_proximidad(arbol_mcu, "strang", "Doctor Strange")
print()

print("--- Punto F: Superhéroes en orden descendente ---")
def listar_heroes_descendente(raiz):
    if raiz is not None:
        listar_heroes_descendente(raiz.right)
        if not raiz.other_values['is_villain']:
            print(raiz.value)
        listar_heroes_descendente(raiz.left)

listar_heroes_descendente(arbol_mcu.root)
print()

print("--- Punto G: Generar un bosque (separar en dos árboles) ---")
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()

def separar_bosque(raiz, arbol_h, arbol_v):
    if raiz is not None:
        if raiz.other_values['is_villain']:
            arbol_v.insert_node(raiz.value, raiz.other_values)
        else:
            arbol_h.insert_node(raiz.value, raiz.other_values)
        separar_bosque(raiz.left, arbol_h, arbol_v)
        separar_bosque(raiz.right, arbol_h, arbol_v)

separar_bosque(arbol_mcu.root, arbol_heroes, arbol_villanos)

def contar_nodos(raiz):
    if raiz is None:
        return 0
    return 1 + contar_nodos(raiz.left) + contar_nodos(raiz.right)

print(f"I. Nodos en el árbol de superhéroes: {contar_nodos(arbol_heroes.root)}")
print(f"   Nodos en el árbol de villanos: {contar_nodos(arbol_villanos.root)}")
print()

def barrido_alfabetico(raiz):
    if raiz is not None:
        barrido_alfabetico(raiz.left)
        print(raiz.value)
        barrido_alfabetico(raiz.right)

print("II. Barrido alfabético del árbol de superhéroes:")
barrido_alfabetico(arbol_heroes.root)
print("\nII. Barrido alfabético del árbol de villanos:")
barrido_alfabetico(arbol_villanos.root)