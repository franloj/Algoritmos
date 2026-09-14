from list_ import List

class Pokemon:
    def __init__(self, name, nivel, tipo, subtipo=None):
        self.name = name
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f"{self.name} (Nvl: {self.nivel}, {self.tipo}/{self.subtipo})"

class Entrenador:
    def __init__(self, name, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.name = name
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas
        
        self.pokemons = List()
        self.pokemons.add_criterion('name', by_name)

    def __str__(self):
        return f"{self.name} | Torneos: {self.torneos_ganados} | G/P: {self.batallas_ganadas}/{self.batallas_perdidas}"

def by_name(item):
    return item.name