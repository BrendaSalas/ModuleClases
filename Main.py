# main.py

from MyClase import MiClase  # Importa la clase desde el archivo mi_clase.py

from bestPracticeMethodsOOP import Alumno

# Crea una instancia de MiClase
mi_objeto = MiClase("Mundo")

objeto = Alumno

# Usa un método de la clase
print(mi_objeto.saludar())

alumno = Alumno()

registro_alumnos = {}

#nombres = []

# Capturar 3 nombres utilizando input()
for i in range(3):
    alumno.set_nombre(input("Nombre del alumno: "))
    alumno.set_apellido_paterno(input("Apellido paterno: "))
    alumno.set_apellido_materno(input("Apellido materno: "))
    alumno.set_no_control(input("Numero de control: "))
    alumno.set_semestre(input("Semestre: "))
    registro_alumnos[i]=alumno

for alumno in registro_alumnos(3):
    print(f"Nombre: {registro_alumnos[i].get_nombre()}")