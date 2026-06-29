from super_heroes_data import superheroes
from list_ import List
from queue_ import Queue

SEP = "-" * 65


class Personaje:
    def __init__(self, data: dict):
        self.name            = data["name"]
        self.alias           = data["alias"]
        self.real_name       = data["real_name"] if data["real_name"] else "N/A"
        self.bio             = data["short_bio"]
        self.first_appearance = data["first_appearance"]
        self.is_villain      = data["is_villain"]

    def __str__(self):
        rol = "Villano" if self.is_villain else "Héroe"
        return (
            f"  [{rol}] {self.name:30s} | "
            f"Real: {self.real_name:35s} | "
            f"Aparición: {self.first_appearance}"
        )


personajes: List = List()

for d in superheroes:
    personajes.append(Personaje(d))

personajes.add_criterion("name",            lambda p: p.name.lower())
personajes.add_criterion("real_name",       lambda p: p.real_name.lower())
personajes.add_criterion("first_appearance", lambda p: p.first_appearance)

print(f"\nTotal de personajes cargados: {personajes.size()}\n")


print(SEP)
print("1. LISTADO ORDENADO ASCENDENTE POR NOMBRE")
print(SEP)

personajes.sort_by_criterion("name")
for i, p in enumerate(personajes, 1):
    print(f"  {i:>3}. {p.name}")


print(f"\n{SEP}")
print("2. POSICIÓN DE 'THE THING' Y 'ROCKET RACCOON'")
print(SEP)

for nombre_buscar in ["the thing", "rocket raccoon"]:
    idx = personajes.search(nombre_buscar, "name")
    if idx is not None:
        print(f"  '{personajes[idx].name}' → posición {idx + 1} (índice {idx})")
    else:
        print(f"  '{nombre_buscar}' no encontrado.")


print(f"\n{SEP}")
print("3. LISTADO DE VILLANOS")
print(SEP)

villanos: List = List()
for p in personajes:
    if p.is_villain:
        villanos.append(p)

print(f"  Total de villanos: {villanos.size()}\n")
villanos.show()


print(f"\n{SEP}")
print("4. COLA DE VILLANOS → APARECIERON ANTES DE 1980")
print(SEP)

cola_villanos: Queue = Queue()
for v in villanos:
    cola_villanos.arrive(v)

villanos_antes_1980: List = List()

while cola_villanos.size() > 0:
    v = cola_villanos.attention()
    if v.first_appearance < 1980:
        villanos_antes_1980.append(v)

villanos_antes_1980.add_criterion("first_appearance", lambda p: p.first_appearance)
villanos_antes_1980.sort_by_criterion("first_appearance")

print(f"  Villanos con primera aparición antes de 1980 ({villanos_antes_1980.size()}):\n")
villanos_antes_1980.show()


print(f"\n{SEP}")
print("5. PERSONAJES QUE COMIENZAN CON: Bl, G, My, W")
print(SEP)

personajes.filter_start_with(("Bl", "G", "My", "W"))


print(f"\n{SEP}")
print("6. LISTADO ORDENADO POR NOMBRE REAL (ascendente)")
print(SEP)

personajes.sort_by_criterion("real_name")
for i, p in enumerate(personajes, 1):
    print(f"  {i:>3}. {p.real_name:35s} → {p.name}")


print(f"\n{SEP}")
print("7. SUPERHÉROES ORDENADOS POR FECHA DE APARICIÓN")
print(SEP)

heroes: List = List()
heroes.add_criterion("first_appearance", lambda p: p.first_appearance)

for p in personajes:
    if not p.is_villain:
        heroes.append(p)

heroes.sort_by_criterion("first_appearance")
for i, p in enumerate(heroes, 1):
    print(f"  {i:>3}. {p.first_appearance}  {p.name}")


print(f"\n{SEP}")
print("8. MODIFICAR NOMBRE REAL DE ANT MAN → Scott Lang")
print(SEP)

encontrado = False
for p in personajes:
    if p.name.lower() == "ant man":
        print(f"  Antes   → real_name: '{p.real_name}'")
        p.real_name = "Scott Lang"
        print(f"  Después → real_name: '{p.real_name}'")
        encontrado = True
        break

if not encontrado:
    print("  Ant Man no encontrado en la lista.")


print(f"\n{SEP}")
print("9. BIOGRAFÍA CONTIENE 'time-traveling' O 'suit'")
print(SEP)

personajes.filter_contain_on_bio(["time-traveling", "suit"])


print(f"\n{SEP}")
print("10. ELIMINAR ELECTRO Y BARON ZEMO")
print(SEP)

for nombre in ["electro", "baron zemo"]:
    personajes.sort_by_criterion("name")
    eliminado = personajes.delete_value(nombre, "name")
    if eliminado:
        print(f"  '{eliminado.name}' encontrado y eliminado:")
        print(f"    Nombre real  : {eliminado.real_name}")
        print(f"    Alias        : {eliminado.alias}")
        print(f"    Aparición    : {eliminado.first_appearance}")
        print(f"    Villano      : {eliminado.is_villain}")
        print(f"    Biografía    : {eliminado.bio}\n")
    else:
        print(f"  '{nombre}' NO estaba en la lista.\n")

print(f"  Total de personajes tras la eliminación: {personajes.size()}")
print(SEP + "\n")
