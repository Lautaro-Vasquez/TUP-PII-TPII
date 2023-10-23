from usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contraseña: str, legajo: int, año_inscripcion_carrera: int) -> None:
        super().__init__(nombre, apellido, email, contraseña)
        self.__legajo = legajo
        self.__año_inscripcion_carrera = año_inscripcion_carrera
        self.__mis_cursos = []

    @property
    def legajo(self) -> int:
        return self.__legajo
    
    @legajo.setter
    def legajo(self, legajo: int):
        self.__legajo = legajo

    @property
    def año_inscripcion_carrera(self) -> int:
        return self.__año_inscripcion_carrera
    
    @año_inscripcion_carrera.setter
    def año_inscripcion_carrera(self, año_inscripcion_carrera: int):
        self.__año_inscripcion_carrera = año_inscripcion_carrera

    @property
    def mis_cursos(self):
        return self.__mis_cursos

    def matricularse(self, curso):
        self.__mis_cursos.append(curso)

    def __str__(self) -> str:
        return super().__str__() + f" Legajo: {self.legajo}. Año de inscripción: {self.año_inscripcion_carrera}"

    def matricularse_en_curso(self, curso: object, contraseña_matriculación: str) -> str:
        if curso in self.__mis_cursos:
            return "Ya estás matriculado en este curso."        
        if contraseña_matriculación == curso.contraseña_matriculacion:
            self.__mis_cursos.append(curso)
            return f"Te has matriculado en el curso: {curso.nombre}."
        else:
            return "La contraseña de matriculación es incorrecta."
