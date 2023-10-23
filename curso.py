import random
import string

class Curso:
    largo_contraseña_matriculacion = 6

    def __init__(self, nombre: str) -> None:
        self.__nombre = nombre
        self.__contraseña_matriculacion = self.generar_contraseña()

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def contraseña_matriculacion(self) -> str:
        return self.__contraseña_matriculacion

    def __str__(self) -> str:
        return f"Materia: {self.__nombre}\nContraseña: {self.__contraseña_matriculacion}"

    @classmethod
    def generar_contraseña(cls) -> str:
        return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(cls.largo_contraseña_matriculacion))
