from datos import cargar_superheroes

heroes = cargar_superheroes()

heroes.delete_value("Linterna Verde", "name")

idx_wolverine = heroes.search("Wolverine", "name")
if idx_wolverine is not None:
    print(f"Año de Wolverine: {heroes[idx_wolverine].year}")

idx_strange = heroes.search("Dr. Strange", "name")
if idx_strange is not None:
    heroes[idx_strange].house = "Marvel"

print("\nCon traje/armadura:")
heroes.filter_contain_on_bio(["traje", "armadura"])

print("\nAnteriores a 1963:")
for h in heroes:
    if h.year < 1963:
        print(f"{h.name} ({h.house})")

print("\nCasas específicas:")
for nombre in ["Capitana Marvel", "Mujer Maravilla"]:
    idx = heroes.search(nombre, "name")
    if idx is not None:
        print(f"{nombre} pertenece a: {heroes[idx].house}")

print("\nInformación detallada:")
for nombre in ["Flash", "Star-Lord"]:
    idx = heroes.search(nombre, "name")
    if idx is not None:
        heroe = heroes[idx]
        print(f"{heroe.name} | Año: {heroe.year} | Casa: {heroe.house} | Bio: {heroe.bio}")

print("\nEmpiezan con B, M o S:")
heroes.filter_start_with(("B", "M", "S"))

conteo = {}
for h in heroes:
    conteo[h.house] = conteo.get(h.house, 0) + 1
print(f"\nConteo por casa: {conteo}")