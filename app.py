from estudiante import Estudiante
from profesor import Profesor
from curso import Curso

lista_cursos = []

lista_estudiantes = [Estudiante("alan", "moex", "alan@gmail.com", "alanmoex", 123, 2023)]
lista_profesores = [Profesor("Juan", "Perez", "juanperez@gmail.com", "juanperez", "licenciado", 2000)]

def menu_principal():
    print("1 - Ingresar como estudiante")
    print("2 - Ingresar como profesor")
    print("3 - Ver cursos")
    print("4 - Salir")

def menu_estudiante(estudiante):
    print("1 - Matricularse en un curso")
    print("2 - Ver cursos matriculados")
    print("3 - Volver al menú principal")

def menu_profesor(profesor):
    print("1 - Dictar curso")
    print("2 - Ver cursos")
    print("3 - Volver al menú principal")

def obtener_opcion_valida():
    while True:
        opcion = input("Ingrese una opción: ")
        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= 4:
                return opcion
            else:
                print("Error: Ingrese una opción válida (1-4).")
        else:
            print("Error: Ingrese un número válido (1-4).")

while True:
    menu_principal()
    op = obtener_opcion_valida()

    if op == 1:
        email = input("Ingrese su email: ")
        contraseña = input("Ingrese su contraseña: ")
        encontrado = False

        for estudiante in lista_estudiantes:
            if estudiante.email == email:
                encontrado = True
                if estudiante.validar_credenciales(email, contraseña):
                    print("Ha ingresado como estudiante\n")
                    while True:
                        menu_estudiante(estudiante)
                        opEst = obtener_opcion_valida()
                        
                        if opEst == 1:
                            if not lista_cursos:
                                print("Advertencia: No hay cursos creados en el sistema.")
                            else:
                                print("Cursos disponibles:")
                                for curso in lista_cursos:
                                    print(f"Curso: {curso.nombre}")
                                nombre_curso = input("Ingrese el nombre del curso a matricularse: ")
                                for curso in lista_cursos:
                                    if curso.nombre == nombre_curso:
                                        contraseña_matriculacion = input("Ingrese la contraseña de matriculación del curso: ")
                                        mensaje = estudiante.matricularse_en_curso(curso, contraseña_matriculacion)
                                        print(mensaje)
                                        break
                                else:
                                    print("Error: El curso no existe.")
                        elif opEst == 2:
                            if not estudiante.mis_cursos:
                                print("No estás matriculado en ningún curso.")
                            else:
                                print("Cursos matriculados:")
                                for curso in estudiante.mis_cursos:
                                    print(f"Curso: {curso.nombre}")
                        elif opEst == 3:
                            break
                else:
                    print("Error: Contraseña incorrecta.")

        if not encontrado:
            print("Usuario no encontrado. Debe darse de alta en alumnado.")
    
    elif op == 2:
        email = input("Ingrese su email: ")
        contraseña = input("Ingrese su contraseña: ")
        encontrado = False

        for profesor in lista_profesores:
            if profesor.email == email:
                encontrado = True
                if profesor.validar_credenciales(email, contraseña):
                    print("Ha ingresado como profesor\n")
                    while True:
                        menu_profesor(profesor)
                        opProf = obtener_opcion_valida()

                        if opProf == 1:
                            nombre_curso = input("Ingrese el nombre del nuevo curso: ")
                            nuevo_curso = Curso(nombre_curso)
                            lista_cursos.append(nuevo_curso)
                            profesor.mis_cursos.append(nuevo_curso)
                            print(f"Has creado el curso: {nuevo_curso}")
                        elif opProf == 2:
                            if not lista_cursos:
                                print("Advertencia: No hay cursos creados en el sistema.")
                            else:
                                print("Cursos existentes:")
                                for curso in lista_cursos:
                                    print(f"Curso: {curso.nombre}, Contraseña: {curso.contraseña_matriculacion}")
                        elif opProf == 3:
                            break
                else:
                    print("Error: Contraseña incorrecta.")

        if not encontrado:
            print("Usuario no encontrado. Debe darse de alta como profesor.")
    
    elif op == 3:
        if not lista_cursos:
            print("Advertencia: No hay cursos creados en el sistema.")
        else:
            cursos_ordenados = sorted(lista_cursos, key=lambda curso: curso.nombre)
            for curso in cursos_ordenados:
                print(f"Curso: {curso.nombre}")
    
    elif op == 4:
        print("Ha elegido salir. Chau")
        break

    else:
        print("Error: opción ingresada incorrecta.")
