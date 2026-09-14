from datos import cargar_entrenadores

entrenadores = cargar_entrenadores()

print("\n--- Cantidad de Pokémons de un entrenador (Ash) ---")
idx = entrenadores.search("Ash", "name")
if idx is not None:
    print(f"Pokémons de Ash: {entrenadores[idx].pokemons.size()}")

print("\n--- Entrenadores con más de 3 torneos ganados ---")
for e in entrenadores:
    if e.torneos_ganados > 3:
        print(e.name)

print("\n--- Pokémon de mayor nivel del entrenador con más torneos ---")
if entrenadores.size() > 0:
    mejor_e = entrenadores[0]
    for e in entrenadores:
        if e.torneos_ganados > mejor_e.torneos_ganados:
            mejor_e = e
    
    if mejor_e.pokemons.size() > 0:
        mejor_p = mejor_e.pokemons[0]
        for p in mejor_e.pokemons:
            if p.nivel > mejor_p.nivel:
                mejor_p = p
        print(f"Entrenador: {mejor_e.name} | Pokémon: {mejor_p}")

print("\n--- Todos los datos de un entrenador y sus Pokémons (Misty) ---")
idx = entrenadores.search("Misty", "name")
if idx is not None:
    print(entrenadores[idx])
    entrenadores[idx].pokemons.show()

print("\n--- Entrenadores con > 79% de batallas ganadas ---")
for e in entrenadores:
    total = e.batallas_ganadas + e.batallas_perdidas
    if total > 0:
        pct = (e.batallas_ganadas / total) * 100
        if pct > 79:
            print(f"{e.name}: {pct:.2f}%")

print("\n--- Entrenadores con tipo (Fuego y Planta) o (Agua/Volador) ---")
for e in entrenadores:
    fuego, planta, agua_volador = False, False, False
    for p in e.pokemons:
        if p.tipo == "Fuego" or p.subtipo == "Fuego": fuego = True
        if p.tipo == "Planta" or p.subtipo == "Planta": planta = True
        if (p.tipo == "Agua" and p.subtipo == "Volador") or (p.tipo == "Volador" and p.subtipo == "Agua"):
            agua_volador = True
    
    if (fuego and planta) or agua_volador:
        print(e.name)

print("\n--- Promedio de nivel de Pokémons de un entrenador (Brock) ---")
idx = entrenadores.search("Brock", "name")
if idx is not None:
    e = entrenadores[idx]
    if e.pokemons.size() > 0:
        promedio = sum(p.nivel for p in e.pokemons) / e.pokemons.size()
        print(f"Promedio de Brock: {promedio:.1f}")

print("\n--- Cuántos entrenadores tienen a Pikachu ---")
count = 0
for e in entrenadores:
    if e.pokemons.search("Pikachu", "name") is not None:
        count += 1
print(f"Entrenadores con Pikachu: {count}")

print("\n--- Entrenadores que tienen Pokémons repetidos ---")
for e in entrenadores:
    nombres = []
    for p in e.pokemons:
        if p.name in nombres:
            print(e.name)
            break 
        nombres.append(p.name)

print("\n--- Entrenadores con Tyrantrum, Terrakion o Wingull ---")
objetivos = ["Tyrantrum", "Terrakion", "Wingull"]
for e in entrenadores:
    encontrado = False
    for p in e.pokemons:
        if p.name in objetivos:
            encontrado = True
            break
    if encontrado:
        print(e.name)

print("\n--- Determinar si entrenador X tiene al Pokémon Y ---")
def buscar_par(nombre_entrenador, nombre_pokemon):
    idx_e = entrenadores.search(nombre_entrenador, "name")
    if idx_e is not None:
        e = entrenadores[idx_e]
        idx_p = e.pokemons.search(nombre_pokemon, "name")
        if idx_p is not None:
            print(f"¡Encontrado!\n{e}\n{e.pokemons[idx_p]}")
        else:
            print(f"{e.name} no tiene a {nombre_pokemon}.")
    else:
        print("Entrenador no encontrado.")

entrenador_ingresado = input("Ingresá el nombre del entrenador (ej. Ash): ")
pokemon_ingresado = input("Ingresá el nombre del Pokémon (ej. Pikachu): ")

buscar_par(entrenador_ingresado, pokemon_ingresado)