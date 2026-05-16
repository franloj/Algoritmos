from stack import Stack

def procesar_mcu(pila_mcu: Stack):
    posicion_rocket = -1
    posicion_groot = -1
    
    mas_de_5_peliculas = []
    
    peliculas_viuda_negra = 0
    
    personajes_cdg = []
    
    pila_aux = Stack()
    
    posicion_actual = 1
    
    while pila_mcu.size() > 0:
        personaje = pila_mcu.pop()
        
        if personaje['nombre'] == 'Rocket Raccoon':
            posicion_rocket = posicion_actual
        elif personaje['nombre'] == 'Groot':
            posicion_groot = posicion_actual
            
        if personaje['peliculas'] > 5:
            mas_de_5_peliculas.append((personaje['nombre'], personaje['peliculas']))
            
        if personaje['nombre'] == 'Black Widow' or personaje['nombre'] == 'Viuda Negra':
            peliculas_viuda_negra = personaje['peliculas']
            
        letra_inicial = personaje['nombre'][0].upper()
        if letra_inicial in ['C', 'D', 'G']:
            personajes_cdg.append(personaje['nombre'])
            
        pila_aux.push(personaje)
        
        posicion_actual += 1
        
    while pila_aux.size() > 0:
        pila_mcu.push(pila_aux.pop())
        
    print("--- Posiciones de Rocket Raccoon y Groot ---")
    if posicion_rocket != -1:
        print(f"Rocket Raccoon se encuentra en la posición: {posicion_rocket}")
    else:
        print("Rocket Raccoon no se encuentra en la pila.")
        
    if posicion_groot != -1:
        print(f"Groot se encuentra en la posición: {posicion_groot}")
    else:
        print("Groot no se encuentra en la pila.")
    print()
    
    print("--- Personajes con más de 5 películas ---")
    if mas_de_5_peliculas:
        for nombre, peliculas in mas_de_5_peliculas:
            print(f"- {nombre} participó en {peliculas} películas.")
    else:
        print("No hay personajes que hayan participado en más de 5 películas.")
    print()
        
    print("--- Películas de Viuda Negra ---")
    if peliculas_viuda_negra > 0:
        print(f"La Viuda Negra (Black Widow) participó en {peliculas_viuda_negra} películas.")
    else:
        print("La Viuda Negra no se encuentra en la pila o participó en 0 películas.")
    print()
        
    print("--- Personajes que empiezan con C, D y G ---")
    if personajes_cdg:
        print("Personajes:")
        for nombre in personajes_cdg:
            print(f"- {nombre}")
    else:
        print("No hay personajes cuyos nombres empiecen con C, D y G.")

if __name__ == "__main__":
    pila_mcu = Stack()
    
    pila_mcu.push({'nombre': 'Iron Man', 'peliculas': 10})
    pila_mcu.push({'nombre': 'Captain America', 'peliculas': 9})
    pila_mcu.push({'nombre': 'Black Widow', 'peliculas': 8})
    pila_mcu.push({'nombre': 'Hulk', 'peliculas': 7})
    pila_mcu.push({'nombre': 'Thor', 'peliculas': 8})
    pila_mcu.push({'nombre': 'Groot', 'peliculas': 4})
    pila_mcu.push({'nombre': 'Rocket Raccoon', 'peliculas': 5})
    pila_mcu.push({'nombre': 'Doctor Strange', 'peliculas': 6})
    pila_mcu.push({'nombre': 'Gamora', 'peliculas': 4})
    pila_mcu.push({'nombre': 'Drax', 'peliculas': 4})
    pila_mcu.push({'nombre': 'Spider-Man', 'peliculas': 6})
    
    procesar_mcu(pila_mcu)
