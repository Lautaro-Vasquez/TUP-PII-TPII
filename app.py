from estudiante import Estudiante
from profesor import Profesor
from curso import Curso

# Crear instancias de cursos y agregarlos a la lista de cursos
curso1 = Curso("Programación I", "contrasenia1")
curso2 = Curso("Programación II", "contrasenia2")
curso3 = Curso("Laboratorio II", "contrasenia3")
curso4 = Curso("InglesI", "contrasenia4")
curso5 = Curso("InglesII", "contrasenia5")

lista_cursos = [curso1, curso2, curso3, curso4, curso5]

# Crear instancias de estudiantes y profesores
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

while True:
    menu_principal()
    op = int(input("Ingrese una opción: "))
    
    if op == 1:
        encontrado = False
        email = input("Ingrese su email: ")
        contraseña = input("Ingrese su contraseña: ")

        for estudiante in lista_estudiantes:
            if estudiante.email == email:
                encontrado = True
                validado = estudiante.validar_credenciales(email, contraseña)

                if validado:
                    print("Ha ingresado correctamente\n")
                    while True:
                        menu_estudiante(estudiante)
                        opEst = int(input("Ingrese una opción: "))
                        
                        if opEst == 1:
                            print("Cursos disponibles:")
                            for i, curso in enumerate(lista_cursos, start=1):
                                print(f"{i} {curso.nombre}")
                            pass
                        elif opEst == 2:
                            pass
                        elif opEst == 3:
                            break

        if not encontrado:
            print("Usuario no encontrado. Debe darse de alta en el alumnado.")

    elif op == 2:
        # Aquí debes implementar la lógica para ingresar como profesor
        encontrado = False
        email = input("Ingrese su email: ")
        contraseña = input("Ingrese su contraseña: ")

        for profesor in lista_profesores:
            if profesor.email == email:
                encontrado = True
                validado = profesor.validar_credenciales(email, contraseña)

                if validado:
                    print("Ha ingresado como profesor correctamente\n")
                    while True:
                        menu_profesor(profesor)
                        opProf = int(input("Ingrese una opción: "))
                        
                        if opProf == 1:
                            # Lógica para dictar un curso
                            nombre_curso = input("Ingrese el nombre del nuevo curso: ")
                            contraseña_matriculación = Curso.generar_contraseña()
                            nuevo_curso = Curso(nombre_curso, contraseña_matriculación)
                            profesor.mis_cursos.append(nuevo_curso)
                            print(f"Has creado el curso: {nuevo_curso.nombre}")
                            print(f"Contraseña de matriculación: {nuevo_curso.contraseña_matriculación}")
                        
                        elif opProf == 2:
                            # Lógica para ver cursos del profesor
                            if not profesor.mis_cursos:
                                print("No tienes cursos disponibles.")
                            else:
                                print("Tus cursos:")
                                for i, curso in enumerate(profesor.mis_cursos, start=1):
                                    print(f"{i} {curso.nombre}")
                        
                        elif opProf == 3:
                            break

        if not encontrado:
            print("Usuario no encontrado. Debe darse de alta como profesor.")
    elif op == 3:
        print("Cursos disponibles:")
        for i, curso in enumerate(lista_cursos, start=1):
            print(f"{i} {curso.nombre}")
    elif op == 4:
        print("Ha elegido salir. ¡Hasta luego!")
        break
    else:
        print("Error: opción ingresada incorrecta.")
