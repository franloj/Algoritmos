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


red = Graph(is_dir=False)


notebooks = ['Red Hat', 'Debian', 'Arch']
pcs = ['Ubuntu', 'Mint', 'Fedora', 'Manjaro', 'Parrot']
servidores = ['Guaraní', 'MongoDB']
switches = ['Switch 1', 'Switch 2']
routers = ['Router 1', 'Router 2', 'Router 3']

for nb in notebooks:
    red.add_vertex(nb, 'notebook')
for pc in pcs:
    red.add_vertex(pc, 'pc')
for srv in servidores:
    red.add_vertex(srv, 'servidor')
for sw in switches:
    red.add_vertex(sw, 'switch')
for rt in routers:
    red.add_vertex(rt, 'router')
red.add_vertex('Impresora', 'impresora')

red.add_edge(17, 'Debian', 'Switch 1')
red.add_edge(18, 'Ubuntu', 'Switch 1')
red.add_edge(22, 'Impresora', 'Switch 1')
red.add_edge(80, 'Mint', 'Switch 1')
red.add_edge(29, 'Switch 1', 'Router 1')

red.add_edge(37, 'Router 1', 'Router 2')
red.add_edge(43, 'Router 1', 'Router 3')
red.add_edge(50, 'Router 2', 'Router 3')

red.add_edge(25, 'Red Hat', 'Router 2')
red.add_edge(9, 'Guaraní', 'Router 2')

red.add_edge(61, 'Router 3', 'Switch 2')
red.add_edge(40, 'Manjaro', 'Switch 2')
red.add_edge(12, 'Parrot', 'Switch 2')
red.add_edge(5, 'MongoDB', 'Switch 2')
red.add_edge(56, 'Arch', 'Switch 2')
red.add_edge(3, 'Fedora', 'Switch 2')


print("=== PUNTO 5.b: Barridos desde las notebooks ===")
for nb in notebooks:
    print(f"\n-> Barrido en PROFUNDIDAD desde {nb}:")
    red.deep_show(nb)
    print(f"\n-> Barrido en AMPLITUD desde {nb}:")
    red.amplitude_show(nb)


print("\n=== PUNTO 5.c: Camino más corto hasta la Impresora ===")
for equipo in ['Manjaro', 'Red Hat', 'Fedora']:
    camino, costo = obtener_camino(red, equipo, 'Impresora')
    print(f"Desde {equipo}: {' -> '.join(camino)} (Costo: {costo})")


print("\n=== PUNTO 5.d: Árbol de expansión mínima (Kruskal) ===")
mst = red.kruskal('Router 1')
peso_total_mst = 0
for arista in mst.split(';'):
    origen, destino, peso = arista.split('-')
    print(f"  {origen} <-> {destino} (Peso: {peso})")
    peso_total_mst += int(peso)
print(f"Peso total del árbol de expansión mínima: {peso_total_mst}")


print("\n=== PUNTO 5.e: Camino más corto desde una PC (no notebook) hasta Guaraní ===")
mejor_pc_guarani = None
menor_costo_guarani = float('inf')
mejor_camino_guarani = []

for nodo in red:
    if nodo.other_values == 'pc':
        camino, costo = obtener_camino(red, nodo.value, 'Guaraní')
        print(f"  Probando PC {nodo.value}: costo {costo} ({' -> '.join(camino)})")
        if costo is not None and costo < menor_costo_guarani:
            menor_costo_guarani = costo
            mejor_pc_guarani = nodo.value
            mejor_camino_guarani = camino

print(f"Resultado: La PC con camino más corto a Guaraní es '{mejor_pc_guarani}' "
      f"con un costo de {menor_costo_guarani} ({' -> '.join(mejor_camino_guarani)}).")


print("\n=== PUNTO 5.f: Computadora del Switch 1 con camino más corto a MongoDB ===")
pos_sw1 = red.search('Switch 1', 'value')
mejor_comp_mongo = None
menor_costo_mongo = float('inf')
mejor_camino_mongo = []

mejor_pc_mongo = None
menor_costo_pc_mongo = float('inf')

for arista in red[pos_sw1].edges:
    pos_vecino = red.search(arista.destination, 'value')
    vecino = red[pos_vecino]
    if vecino.other_values in ['pc', 'notebook']:
        camino, costo = obtener_camino(red, vecino.value, 'MongoDB')
        print(f"  Probando {vecino.value} ({vecino.other_values}): costo {costo} ({' -> '.join(camino)})")
        if costo is not None and costo < menor_costo_mongo:
            menor_costo_mongo = costo
            mejor_comp_mongo = vecino.value
            mejor_camino_mongo = camino
        if vecino.other_values == 'pc' and costo is not None and costo < menor_costo_pc_mongo:
            menor_costo_pc_mongo = costo
            mejor_pc_mongo = vecino.value

print(f"Resultado general (incluyendo notebooks): '{mejor_comp_mongo}' con costo {menor_costo_mongo} ({' -> '.join(mejor_camino_mongo)}).")
print(f"Resultado considerando solo PC de escritorio: '{mejor_pc_mongo}' con costo {menor_costo_pc_mongo}.")


print("\n=== PUNTO 5.g: Cambio de Impresora a Router 2 y nuevos barridos ===")
arista_eliminada = red.delete_edge('Impresora', 'Switch 1')
peso_impresora = arista_eliminada.weight if arista_eliminada else 22
red.add_edge(peso_impresora, 'Impresora', 'Router 2')

for nb in notebooks:
    print(f"\n-> NUEVO Barrido en PROFUNDIDAD desde {nb}:")
    red.deep_show(nb)
    print(f"\n-> NUEVO Barrido en AMPLITUD desde {nb}:")
    red.amplitude_show(nb)