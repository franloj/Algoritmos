from list_ import List
from modelos import Pokemon, Entrenador, by_name

def cargar_entrenadores():
    entrenadores = List()
    entrenadores.add_criterion('name', by_name)

    ash = Entrenador("Ash", 5, 20, 150)
    ash.pokemons.append(Pokemon("Pikachu", 50, "Eléctrico", None))
    ash.pokemons.append(Pokemon("Charizard", 60, "Fuego", "Volador"))
    ash.pokemons.append(Pokemon("Bulbasaur", 30, "Planta", "Veneno"))
    ash.pokemons.append(Pokemon("Pikachu", 10, "Eléctrico", None)) 

    misty = Entrenador("Misty", 1, 30, 40)
    misty.pokemons.append(Pokemon("Starmie", 40, "Agua", "Psíquico"))
    misty.pokemons.append(Pokemon("Gyarados", 55, "Agua", "Volador"))

    brock = Entrenador("Brock", 4, 15, 65) 
    brock.pokemons.append(Pokemon("Onix", 45, "Roca", "Tierra"))
    brock.pokemons.append(Pokemon("Wingull", 20, "Agua", "Volador"))
    brock.pokemons.append(Pokemon("Tyrantrum", 50, "Roca", "Dragón"))

    entrenadores.append(ash)
    entrenadores.append(misty)
    entrenadores.append(brock)
    
    return entrenadores