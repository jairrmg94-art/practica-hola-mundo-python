"""
Programa: Hola Mundo (Paradigma Orientado a Datos)
Autor: [Tu nombre]
Descripción:
Este programa utiliza el paradigma orientado a datos, donde la información se almacena en estructuras
de datos y el programa se centra en su manipulación.
"""

# Definición de la estructura de datos
datos = {
    "mensaje": "Hola Mundo"
}

def obtener_mensaje(data):
    """
    Extrae el mensaje desde la estructura de datos.
    """
    return data["mensaje"]

def mostrar_mensaje(mensaje):
    """
    Imprime el mensaje en consola.
    """
    print(mensaje)

# Flujo principal del programa
if __name__ == "__main__":
    mensaje = obtener_mensaje(datos)  # Se obtiene el dato desde la estructura
    mostrar_mensaje(mensaje)          # Se muestra en pantalla