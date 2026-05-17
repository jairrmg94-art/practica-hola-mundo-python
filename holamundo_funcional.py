"""
Programa: Hola Mundo (Paradigma Funcional)
Autor: [Tu nombre]
Descripción:
Este programa utiliza el paradigma funcional, donde la lógica se divide en funciones pequeñas
que reciben datos y devuelven resultados sin depender de estados externos.
"""

# Función que genera el mensaje
def crear_mensaje():
    """
    Retorna un mensaje de saludo.
    No depende de variables externas (función pura).
    """
    return "Hola Mundo"

# Función que imprime el mensaje
def mostrar_mensaje(mensaje):
    """
    Recibe un mensaje como parámetro y lo imprime en consola.
    """
    print(mensaje)

# Flujo principal del programa
if __name__ == "__main__":
    mensaje = crear_mensaje()   # Se obtiene el mensaje
    mostrar_mensaje(mensaje)    # Se muestra en pantalla