
import pandas as pd
import json
from collections import defaultdict
import matplotlib.pyplot as plt
import os


def grf_prom_edad(promedios):
    paises = list(promedios.keys())
    generos = set()

    # Obtener todos los géneros presentes en los datos
    for pais in paises:
        for genero in promedios[pais]:
            generos.add(genero)

    for genero in generos:
        edades = [promedios[pais].get(genero, 0) for pais in paises]  # Usar get para manejar claves ausentes
        plt.bar(paises, edades, label=genero)

    plt.xlabel('País')
    plt.ylabel('Edad promedio')
    plt.title('Promedio de edad por género y país')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Función para graficar el nivel de educación de mujeres mayores de 18 años por país
def grf_nivel_educacion_mujeres(datos):
    paises = list(datos.keys())
    educacion_mujeres_mayores = [datos[pais]['Mujer'] for pais in paises]

    plt.bar(paises, educacion_mujeres_mayores, color='orange')
    plt.xlabel('País')
    plt.ylabel('Cantidad de mujeres mayores con educación')
    plt.title('Nivel de educación de mujeres mayores de 18 por país')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Función para graficar el porcentaje de hombres y mujeres
def grf_generos(datos):
    labels = list(datos['Todos'].keys())
    sizes = [len(datos['Todos'][label]) for label in labels]
    colors = ['blue', 'pink']  # Puedes cambiar los colores si lo deseas
    explode = (0, 0.1)  # Separa la porción de la mujer para destacarla

    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Asegura que el gráfico de pastel sea un círculo
    plt.title('Porcentaje de hombres y mujeres')
    plt.show()