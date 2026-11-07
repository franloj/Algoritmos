from graph import Graph

def obtener_camino(grafo, origen, destino):
    """Extrae el camino más corto y su costo desde la pila que devuelve dijkstra."""
    if not grafo.exist_path(origen, destino):
        return [], None
    
    paths = grafo.dijkstra(origen)
    costo_total = None
    camino = []
    nodo_actual = destino
    
    while paths.size() > 0:
        value = paths.pop()
        if value[0] == nodo_actual:
            if costo_total is None:
                costo_total = value[1]
            camino.append(value[0])
            nodo_actual = value[2]
            
    camino.reverse()
    return camino, costo_total


casa = Graph(is_dir=False)

ambientes = [
    "cocina", "comedor", "cochera", "quincho", "baño 1",
    "baño 2", "habitación 1", "habitación 2", "sala de estar",
    "terraza", "patio"
]

for ambiente in ambientes:
    casa.add_vertex(ambiente)

casa.add_edge(2, "cocina", "comedor")
casa.add_edge(4, "cocina", "sala de estar")
casa.add_edge(3, "cocina", "baño 1")
casa.add_edge(5, "cocina", "patio")
casa.add_edge(7, "cocina", "cochera")

casa.add_edge(3, "comedor", "sala de estar")
casa.add_edge(4, "comedor", "baño 2")
casa.add_edge(6, "comedor", "terraza")
casa.add_edge(5, "comedor", "habitación 1")

casa.add_edge(6, "cochera", "patio")
casa.add_edge(8, "cochera", "sala de estar")

casa.add_edge(4, "quincho", "patio")
casa.add_edge(5, "quincho", "terraza")
casa.add_edge(3, "quincho", "baño 2")

casa.add_edge(2, "baño 1", "habitación 1")
casa.add_edge(4, "baño 1", "sala de estar")

casa.add_edge(2, "baño 2", "habitación 2")

casa.add_edge(4, "habitación 1", "habitación 2")

casa.add_edge(3, "habitación 2", "terraza")

print("=== Verificación de cantidad de aristas por ambiente (Punto 14.b) ===")
for vertice in casa:
    print(f"  {vertice.value}: {len(vertice.edges)} aristas")


print("\n=== PUNTO 14.c: Árbol de expansión mínima (Kruskal) ===")
mst = casa.kruskal("cocina")
metros_totales_mst = 0

for arista in mst.split(';'):
    origen, destino, peso = arista.split('-')
    print(f"  {origen} <-> {destino}: {peso} m")
    metros_totales_mst += int(peso)

print(f"\nTotal de metros de cable necesarios para conectar todos los ambientes: {metros_totales_mst} metros.")


print("\n=== PUNTO 14.d: Camino más corto de 'habitación 1' a 'sala de estar' (Dijkstra) ===")
camino, metros_cable_red = obtener_camino(casa, "habitación 1", "sala de estar")

print(f"Camino más corto: {' -> '.join(camino)}")
print(f"Se necesitan {metros_cable_red} metros de cable de red para conectar el router con el Smart Tv.")