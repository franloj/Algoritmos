from queue_ import Queue
from stack import Stack

class Notificacion:
    def __init__(self, hora: str, aplicacion: str, mensaje: str):
        self.hora = hora
        self.aplicacion = aplicacion
        self.mensaje = mensaje

    def __str__(self):
        return f"[{self.hora}] {self.aplicacion}: {self.mensaje}"

def eliminar_notificaciones_facebook(cola: Queue):
    tamanio = cola.size()
    for _ in range(tamanio):
        notificacion = cola.attention()
        if notificacion.aplicacion != 'Facebook':
            cola.arrive(notificacion)

def mostrar_notificaciones_twitter_python(cola: Queue):
    tamanio = cola.size()
    for _ in range(tamanio):
        notificacion = cola.attention()
        if notificacion.aplicacion == 'Twitter' and 'Python' in notificacion.mensaje:
            print(notificacion)
        cola.arrive(notificacion)

def contar_notificaciones_rango_tiempo(cola: Queue, hora_inicio: str, hora_fin: str) -> int:
    pila = Stack()
    tamanio = cola.size()
    for _ in range(tamanio):
        notificacion = cola.attention()
        if hora_inicio <= notificacion.hora <= hora_fin:
            pila.push(notificacion)
        cola.arrive(notificacion)
    
    return pila.size()

if __name__ == "__main__":
    cola_notificaciones = Queue()
    
    cola_notificaciones.arrive(Notificacion("10:30", "WhatsApp", "Hola, ¿cómo estás?"))
    cola_notificaciones.arrive(Notificacion("11:45", "Facebook", "A Juan le gusta tu foto"))
    cola_notificaciones.arrive(Notificacion("12:15", "Twitter", "Aprender Python es genial"))
    cola_notificaciones.arrive(Notificacion("14:20", "Instagram", "Nuevo seguidor"))
    cola_notificaciones.arrive(Notificacion("15:00", "Twitter", "Nuevo tutorial de Python disponible"))
    cola_notificaciones.arrive(Notificacion("15:50", "Facebook", "Tienes un nuevo mensaje"))
    cola_notificaciones.arrive(Notificacion("16:05", "Twitter", "Noticias de tecnología"))
    
    print("--- Notificaciones originales ---")
    cola_notificaciones.show()
    print()
    
    print("--- a. Eliminando notificaciones de Facebook ---")
    eliminar_notificaciones_facebook(cola_notificaciones)
    cola_notificaciones.show()
    print()
    
    print("--- b. Notificaciones de Twitter que incluyen 'Python' ---")
    mostrar_notificaciones_twitter_python(cola_notificaciones)
    print()
    
    print("--- c. Notificaciones entre las 11:43 y las 15:57 ---")
    cantidad = contar_notificaciones_rango_tiempo(cola_notificaciones, "11:43", "15:57")
    print(f"Cantidad de notificaciones en ese rango (11:43 - 15:57): {cantidad}")
