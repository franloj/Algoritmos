from stack import Stack

def procesar_bitacoras(pila_boba: Stack, pila_din: Stack):
    planetas_boba = []
    planetas_din = []
    
    creditos_boba = 0
    creditos_din = 0
    
    mision_han_solo = -1
    
    capturas_boba = 0
    capturas_din = 0
    
    pila_aux_boba = Stack()
    while pila_boba.size() > 0:
        pila_aux_boba.push(pila_boba.pop())
        
    numero_mision = 1
    while pila_aux_boba.size() > 0:
        mision = pila_aux_boba.pop()
        
        planetas_boba.append(mision['planeta'])
        
        creditos_boba += mision['recompensa']
        
        if mision['capturado'] == 'Han Solo':
            mision_han_solo = numero_mision
            
        if mision['capturado'].lower() not in ['nadie', 'ninguno', '']:
            capturas_boba += 1
            
        pila_boba.push(mision)
        numero_mision += 1

    pila_aux_din = Stack()
    while pila_din.size() > 0:
        pila_aux_din.push(pila_din.pop())
        
    while pila_aux_din.size() > 0:
        mision = pila_aux_din.pop()
        
        planetas_din.append(mision['planeta'])
        
        creditos_din += mision['recompensa']
        
        if mision['capturado'].lower() not in ['nadie', 'ninguno', '']:
            capturas_din += 1
            
        pila_din.push(mision)

    print("--- A. Planetas visitados (en el orden que hicieron las misiones) ---")
    print(f"Boba Fett : {', '.join(planetas_boba)}")
    print(f"Din Djarin: {', '.join(planetas_din)}")
    print()
    
    print("--- B. Recaudación total ---")
    print(f"Boba Fett : {creditos_boba} créditos")
    print(f"Din Djarin: {creditos_din} créditos")
    if creditos_boba > creditos_din:
        print("-> Boba Fett obtuvo mayor fortuna.")
    elif creditos_din > creditos_boba:
        print("-> Din Djarin obtuvo mayor fortuna.")
    else:
        print("-> Ambos obtuvieron la misma fortuna.")
    print()
        
    print("--- C. Misión de captura de Han Solo ---")
    if mision_han_solo != -1:
        print(f"Boba Fett capturó a Han Solo en la misión número {mision_han_solo} (desde el fondo de la pila).")
    else:
        print("Boba Fett no capturó a Han Solo en las misiones registradas.")
    print()
        
    print("--- D. Cantidad de capturas realizadas ---")
    print(f"Boba Fett : {capturas_boba} capturas")
    print(f"Din Djarin: {capturas_din} capturas")


if __name__ == "__main__":
    pila_boba = Stack()
    pila_din = Stack()

    pila_boba.push({'planeta': 'Kamino', 'capturado': 'Fugitivo Clon', 'recompensa': 5000})
    pila_boba.push({'planeta': 'Tatooine', 'capturado': 'Han Solo', 'recompensa': 250000})
    pila_boba.push({'planeta': 'Geonosis', 'capturado': 'Droide B1', 'recompensa': 2000})
    pila_boba.push({'planeta': 'Coruscant', 'capturado': 'Nadie', 'recompensa': 0})

    pila_din.push({'planeta': 'Nevarro', 'capturado': 'Mythrol', 'recompensa': 5000})
    pila_din.push({'planeta': 'Arvala-7', 'capturado': 'Nadie', 'recompensa': 0})
    pila_din.push({'planeta': 'Tatooine', 'capturado': 'Fennec Shand', 'recompensa': 10000})
    pila_din.push({'planeta': 'Corvus', 'capturado': 'Morgan Elsbeth', 'recompensa': 45000})
    pila_din.push({'planeta': 'Mandalore', 'capturado': 'Nadie', 'recompensa': 0})
    
    procesar_bitacoras(pila_boba, pila_din)
