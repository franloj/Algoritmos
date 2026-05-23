from queue_ import Queue

mcu_queue = Queue()

characters = [
    {"character_name": "Tony Stark", "superhero_name": "Iron Man", "gender": "M"},
    {"character_name": "Steve Rogers", "superhero_name": "Capitán América", "gender": "M"},
    {"character_name": "Natasha Romanoff", "superhero_name": "Black Widow", "gender": "F"},
    {"character_name": "Carol Danvers", "superhero_name": "Capitana Marvel", "gender": "F"},
    {"character_name": "Scott Lang", "superhero_name": "Ant-Man", "gender": "M"},
    {"character_name": "Wanda Maximoff", "superhero_name": "Scarlet Witch", "gender": "F"},
    {"character_name": "Stephen Strange", "superhero_name": "Doctor Strange", "gender": "M"},
    {"character_name": "Peter Parker", "superhero_name": "Spider-Man", "gender": "M"}
]

for char in characters:
    mcu_queue.arrive(char)

captain_marvel_char = None
female_superheroes = []
male_characters = []
scott_lang_hero = None
s_name_data = []
carol_danvers_found = False
carol_danvers_hero = None

for _ in range(mcu_queue.size()):
    char = mcu_queue.attention()
    
    char_name = char["character_name"]
    hero_name = char["superhero_name"]
    gender = char["gender"]
    
    if hero_name == "Capitana Marvel":
        captain_marvel_char = char_name
        
    if gender == "F":
        female_superheroes.append(hero_name)
        
    if gender == "M":
        male_characters.append(char_name)
        
    if char_name == "Scott Lang":
        scott_lang_hero = hero_name
        
    if char_name.startswith("S") or hero_name.startswith("S"):
        s_name_data.append(char)
        
    if char_name == "Carol Danvers":
        carol_danvers_found = True
        carol_danvers_hero = hero_name
        
    mcu_queue.arrive(char)

print("Nombre del personaje de Capitana Marvel:", captain_marvel_char)
print("")
print("Nombres de los superhéroes femeninos:")
for hero in female_superheroes:
    print(f"- {hero}")
print("")
print("Nombres de los personajes masculinos:")
for name in male_characters:
    print(f"- {name}")
print("")
print("Nombre del superhéroe de Scott Lang:", scott_lang_hero)
print("")
print("Datos de superhéroes o personajes que comienzan con 'S':")
for data in s_name_data:
    print(f"- Personaje: {data['character_name']}, Superhéroe: {data['superhero_name']}, Género: {data['gender']}")
print("")
print("¿Carol Danvers está en la cola?")
if carol_danvers_found:
    print(f"Sí, su nombre de superhéroe es: {carol_danvers_hero}")
else:
    print("No")
