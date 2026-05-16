from stack import Stack

def invert_direction(direction):
    inversions = {
        "norte": "sur",
        "sur": "norte",
        "este": "oeste",
        "oeste": "este",
        "noreste": "suroeste",
        "suroeste": "noreste",
        "noroeste": "sureste",
        "sureste": "noroeste"
    }
    return inversions.get(direction.lower())

def record_movements():
    stack = Stack()
    print("Ingrese los movimientos del robot. Ingrese 'fin' como direccion para terminar.")
    
    while True:
        direction = input("Dirección (norte, sur, este, oeste, noreste, noroeste, sureste, suroeste o 'fin'): ").lower()
        if direction == 'fin':
            break
        
        if direction not in ["norte", "sur", "este", "oeste", "noreste", "noroeste", "sureste", "suroeste"]:
            print("Dirección no válida.")
            continue
            
        try:
            steps = int(input("Cantidad de pasos: "))
            if steps <= 0:
                print("La cantidad de pasos debe ser mayor a 0.")
                continue
        except ValueError:
            print("Por favor, ingrese un número válido para los pasos.")
            continue
            
        stack.push({'direccion': direction, 'pasos': steps})
        print(f"Movimiento registrado: {steps} pasos hacia el {direction}.")

    return stack

def return_to_start(stack):
    print("\n--- Secuencia para volver al punto de partida ---")
    if stack.size() == 0:
        print("El robot no realizó ningún movimiento.")
        return

    while stack.size() > 0:
        movement = stack.pop()
        inverse_dir = invert_direction(movement['direccion'])
        print(f"Mover {movement['pasos']} pasos hacia el {inverse_dir}")

if __name__ == "__main__":
    movements_stack = record_movements()
    return_to_start(movements_stack)
