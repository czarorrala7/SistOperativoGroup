import pandas as pd
import json
from collections import defaultdict
import matplotlib.pyplot as plt
import os


#Lectura de archivos
def fn_cargarjsons(ruta_base):
    datos = defaultdict(lambda: defaultdict(list))

    for archivo in os.listdir(ruta_base):
        if archivo.endswith(".json"):
            with open(os.path.join(ruta_base, archivo)) as file:
                data = json.load(file)
                for usuario_id, info in data.items():
                    pais = info['informacion_personal']['lugar_nacimiento'].split(", ")[0]
                    genero = info['informacion_personal']['genero']
                    edad = info['informacion_personal']['edad']
                    datos[pais][genero].append(edad)

    return datos

# Esta función calcula el promedio de edad por género, agrupado por país
def fn_promedio_edad(datos):
    promedios = defaultdict(dict)

    for pais, generos in datos.items():
        for genero, edades in generos.items():
            promedio = sum(edades) / len(edades) if len(edades) > 0 else 0
            promedios[pais][genero] = promedio

    return promedios


# Esta función lee los archivos JSON de una ruta y devuelve un diccionario con la estructura deseada
def fn_json_estudios(ruta_base):
    datos = defaultdict(lambda: defaultdict(list))

    for archivo in os.listdir(ruta_base):
        if archivo.endswith(".json"):
            with open(os.path.join(ruta_base, archivo)) as file:
                data = json.load(file)
                for usuario_id, info in data.items():
                    pais = info['informacion_personal']['lugar_nacimiento'].split(", ")[0]
                    genero = info['informacion_personal']['genero']
                    edad = info['informacion_personal']['edad']
                    nivel_educacion = info['informacion_demografica'].get('nivel_educacion', None)
                    if nivel_educacion and edad > 18:  # Solo considerar mayores de 18 años
                        datos[pais][genero].append(nivel_educacion)

    return datos

# Esta función calcula el nivel de educación de mujeres mayores de 18 años por país
def fn_nivel_educacion_mujeres(datos):
    educacion_mujeres_mayores = defaultdict(dict)

    for pais, generos in datos.items():
        educacion_mujeres_mayores[pais]['Mujer'] = len(generos.get('Femenino', []))

    return educacion_mujeres_mayores


# Esta función lee los archivos JSON de una ruta y devuelve un diccionario con la estructura deseada
def fn_json_genero(ruta_base):
    datos = defaultdict(lambda: defaultdict(list))

    for archivo in os.listdir(ruta_base):
        if archivo.endswith(".json"):
            with open(os.path.join(ruta_base, archivo)) as file:
                data = json.load(file)
                for usuario_id, info in data.items():
                    genero = info['informacion_personal']['genero']
                    datos['Todos'][genero].append(usuario_id)

    return datos