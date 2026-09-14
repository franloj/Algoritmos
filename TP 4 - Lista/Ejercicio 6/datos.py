from list_ import List
from modelos import Superheroe, by_name

def cargar_superheroes():
    heroes = List()
    heroes.add_criterion('name', by_name)

    heroes.append(Superheroe("Linterna Verde", 1940, "DC", "Anillo de poder"))
    heroes.append(Superheroe("Wolverine", 1974, "Marvel", "Mutante con garras de adamantium"))
    heroes.append(Superheroe("Dr. Strange", 1963, "DC", "Hechicero Supremo")) 
    heroes.append(Superheroe("Iron Man", 1963, "Marvel", "Multimillonario con armadura de alta tecnología"))
    heroes.append(Superheroe("Capitana Marvel", 1967, "Marvel", "Poderes cósmicos y traje kree"))
    heroes.append(Superheroe("Mujer Maravilla", 1941, "DC", "Princesa amazona"))
    heroes.append(Superheroe("Flash", 1940, "DC", "El hombre más rápido, usa traje rojo"))
    heroes.append(Superheroe("Star-Lord", 1976, "Marvel", "Líder de los guardianes"))
    heroes.append(Superheroe("Batman", 1939, "DC", "Caballero oscuro con armadura táctica"))
    heroes.append(Superheroe("Spiderman", 1962, "Marvel", "Sentido arácnido"))

    return heroes