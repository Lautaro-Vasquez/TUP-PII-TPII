from usuario import Usuario

class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contraseña: str, titulo: str, año_egreso: int) -> None:
        super().__init__(nombre, apellido, email, contraseña)
        self.__titulo = titulo
        self.__año_egreso = año_egreso
    
    #getter y setter de titulo
    @property
    def titulo(self) -> str:
        return self.__titulo
    @titulo.setter
    def titulo(self, titulo:str):
        self.__titulo = titulo

    #getter y setter de año_egreso
    @property
    def año_egreso(self) -> int:
        return self.__año_egreso
    @año_egreso.setter
    def año_egreso(self, año_egreso:int):
        self.__año_egreso = año_egreso

    def __str__(self) -> str:
        return super().__str__() + f" Titulo: {self.titulo}. Año de egreso: {self.año_egreso}"


