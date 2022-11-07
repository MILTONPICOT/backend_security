from abc import ABCMeta


class AbstractModel(metaclass=ABCMeta):

    def __init__(self, data: dict):
        for key, value in data.items():  # Convertir clave valor en un listado de tuplas
            setattr(self, key, value)
