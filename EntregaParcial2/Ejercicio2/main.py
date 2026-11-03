from graph import Graph
import json

with open('datos.json', 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)
    personajes = datos["personajes"]
    relaciones = datos["relaciones"]

grafo = Graph(is_dir=False)

for p in personajes:
    grafo.add_vertex(p["nombre"], p)

for p1, p2, episodios in relaciones:
    grafo.add_edge(episodios, p1, p2)

print("\n--- Árbol de expansión mínimo (Kruskal) ---")
for origen in ["C3PO", "Yoda", "Leia"]:
    print(f"\nDesde el vértice {origen}:")
    arbol_min = grafo.kruskal(origen)
    
    if isinstance(arbol_min, str):
        for arista in arbol_min.split(';'):
            origen_a, destino_a, peso_a = arista.split('-')
            print(f"  {origen_a} <-> {destino_a} (Costo/Episodios: {peso_a})")
    else:
        print("  El grafo es disconexo o no se encontró el árbol.")


print("\n--- Número máximo de episodios compartidos y pares ---")
max_episodios = 0
pares_maximos = set() 

for vertice in grafo:
    for arista in vertice.edges:
        if arista.weight > max_episodios:
            max_episodios = arista.weight
            pares_maximos = {frozenset([vertice.value, arista.destination])}
        elif arista.weight == max_episodios:
            pares_maximos.add(frozenset([vertice.value, arista.destination]))

print(f"El número máximo de episodios compartidos es: {max_episodios}")
print("Los personajes que comparten este número son:")
for par in pares_maximos:
    p1, p2 = list(par)
    print(f" - {p1} y {p2}")


print("\n--- Camino más corto (Dijkstra) ---")

def calcular_y_mostrar_camino(origen, destino):
    if grafo.exist_path(origen, destino):
        paths = grafo.dijkstra(origen)
        dest = destino
        peso_total = None
        camino_completo = []

        while paths.size() > 0:
            value = paths.pop()
            if value[0] == dest:
                if peso_total is None:
                    peso_total = value[1]
                camino_completo.append(value[0])
                dest = value[2]
        
        camino_completo.reverse()
        camino_str = " -> ".join(camino_completo)
        print(f"De {origen} a {destino}:\n   Ruta: {camino_str}\n   Costo total: {peso_total}")
    else:
        print(f"No existe un camino posible entre {origen} y {destino}.")

calcular_y_mostrar_camino("C3PO", "R2D2")
calcular_y_mostrar_camino("Yoda", "Darth Vader")


print("\n--- Personajes que aparecieron en los nueve episodios ---")
encontrados = False
for vertice in grafo:
    if vertice.other_values["episodios_totales"] == 9:
        print(f" - {vertice.value}")
        encontrados = True

if not encontrados:
    print(" - Ninguno (con los datos actuales)")

print("\n=================================================================\n")