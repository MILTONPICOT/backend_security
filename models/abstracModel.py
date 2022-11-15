from abc import ABCMeta


class AbstracModel(metaclass=ABCMeta):

# este codigo lo que hace es coger un diccionario y convertir el diccionario en un objeto y
# cada clave del diccionario se va a convertir en un atributo con su respectivo valor guardado

    def __init__(self, data: dict):
        for key, value in data.items():  # items convierte el diccionario clave valor en una lista de tuplas
            setattr(self, key, value) # Convierte en atributos de la clase
