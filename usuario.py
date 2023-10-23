from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre: str, apellido: str, email: str, contraseña: str) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contraseña = contraseña

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def apellido(self) -> str:
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido: str):
        self.__apellido = apellido

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def contraseña(self) -> str:
        return self.__contraseña

    @contraseña.setter
    def contraseña(self, contraseña: str):
        self.__contraseña = contraseña

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}. Apellido: {self.apellido}. Email: {self.email}. Contraseña: {self.contraseña}."

    def validar_credenciales(self, email: str, contraseña: str) -> bool:
        return email == self.email and contraseña == self.contraseña

    # Agregar aquí otros métodos o atributos necesarios para el trabajo práctico.
    # Por ejemplo, si necesitas rastrear a los alumnos o profesores, podrías incluir
    # listas para almacenar sus datos.
