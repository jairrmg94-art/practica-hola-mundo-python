"""
Programa: Hola Mundo (Paradigma Orientado a Objetos)
Autor: [Tu nombre]
Descripción:
Este programa utiliza el paradigma orientado a objetos, donde se encapsulan datos y comportamientos
dentro de una clase.
"""

# Definición de la clase
class Saludo:
    """
    Clase que representa un saludo.
    """

    def __init__(self, mensaje):
        """
        Constructor de la clase.
        Inicializa el atributo mensaje.
        """
        self.mensaje = mensaje

    def mostrar(self):
        """
        Método que imprime el mensaje almacenado en el objeto.
        """
        print(self.mensaje)

# Flujo principal del programa
if __name__ == "__main__":
    saludo = Saludo("Hola Mundo")  # Se crea un objeto de la clase
    saludo.mostrar()               # Se llama al método del objeto