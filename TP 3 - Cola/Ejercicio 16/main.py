from heap import Heap

cola_impresion = Heap()

cola_impresion.arrive("Documento Empleado 1", 1)
cola_impresion.arrive("Documento Empleado 2", 1)
cola_impresion.arrive("Documento Empleado 3", 1)

print("--- Inciso B: Primer documento de la cola ---")
print(cola_impresion.attention()[1])

cola_impresion.arrive("Documento Staff TI 1", 2)
cola_impresion.arrive("Documento Staff TI 2", 2)

cola_impresion.arrive("Documento Gerente 1", 3)

print("\n--- Inciso E: Los dos primeros documentos de la cola ---")
print(cola_impresion.attention()[1])
print(cola_impresion.attention()[1])

cola_impresion.arrive("Documento Empleado 4", 1)
cola_impresion.arrive("Documento Empleado 5", 1)
cola_impresion.arrive("Documento Gerente 2", 3)

print("\n--- Inciso G: Resto de la cola de impresión ---")
while cola_impresion.size() > 0:
    print(cola_impresion.attention()[1])