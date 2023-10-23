import random
import string

class Curso:
    largo_contraseña_matriculacion = 6

    def __init__(self, nombre: str, contraseña_matriculacion: str = None) -> None:
        self.__nombre = nombre
        if contraseña_matriculacion is None:
            contraseña_matriculacion = self.generar_contraseña()
        self.__contraseña_matriculacion = contraseña_matriculacion
    
    #getter y setter de nombre
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre:str):
        self.__nombre = nombre

    #getter y setter de contraseña_matriculacion
    @property
    def contraseña_matriculacion(self) -> str:
        return self.__contraseña_matriculacion
    @contraseña_matriculacion.setter
    def contraseña_matriculacion(self, contraseña_matriculacion:str):
        self.__contraseña_matriculacion = contraseña_matriculacion

    def __str__(self) -> str:
        return f"Curso: {self.__nombre}. Contraseña de matriculación: {self.__contraseña_matriculacion}"
    
    @classmethod
    def generar_contraseña(cls) -> str:
        return(
            "".join(
                random.choice(string.ascii_letters + string.digits)
                for _ in range(cls.largo_contraseña_matriculacion)
            )
        )
