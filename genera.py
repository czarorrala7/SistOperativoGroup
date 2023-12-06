import json
from datetime import datetime

# Función para obtener un ID único para cada persona
def obtener_id(i):
    fecha_hora_actual = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{fecha_hora_actual}_{i}"

# Función para crear un archivo JSON con información simulada de personas
def crear_json(numero):
    # Lista para almacenar los datos de las personas
    datos = []

    # Bucle para generar información para el número de personas especificado
    for i in range(1, numero + 1):
        # Crear un diccionario con información simulada de una persona
        persona = {
            "id": obtener_id(i),
            "nombre": f"Nombre{i}",
            "nacionalidad": f"Nacionalidad{i}",
            "cedula": f"Cedula{i}",
            "direccion": f"Direccion{i}",
            "telefono": f"Telefono{i}",
            "correo": f"Correo{i}@example.com"
        }

        # Agregar el diccionario a la lista de datos
        datos.append(persona)

    # Guardar la lista de datos en un archivo JSON llamado "salida.json"
    with open('salida.json', 'w') as archivo:
        json.dump(datos, archivo, indent=2)

# Solicitar al usuario ingresar el número de personas que desea generar
numero_personas = int(input("Ingrese el número de personas: "))

# Llamar a la función para crear el archivo JSON con la cantidad especificada de personas
crear_json(numero_personas)
