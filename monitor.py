import subprocess
import time

# Nombres de los archivos de los nodos
nodos = ["ejecucion1.py", "ejecucion2.py", "ejecucion3.py"]

# Nombre del archivo de salida
archivo_salida = "estado_nodos.txt"

# Función para obtener el estado de un nodo
def obtener_estado(nodo_nombre):
    try:
        # Utiliza el comando pgrep para buscar el proceso que contiene el nombre del nodo
        resultado = subprocess.run(['pgrep', '-af', nodo_nombre], capture_output=True, text=True, check=True)
        if resultado.stdout:
            return "activo"
        return "apagado"
    except subprocess.CalledProcessError:
        # Si hay un error al ejecutar el comando pgrep, devuelve "apagado"
        return "apagado"

# Función para escribir el estado en el archivo
def escribir_estado():
    a = 0
    with open(archivo_salida, "w") as archivo:
        for i, nodo_nombre in enumerate(nodos):
            estado = obtener_estado(nodo_nombre)
            if estado == "activo":
                if a == 0:
                    archivo.write(f"Nodo{i + 1}=lider\n")
                else:
                    archivo.write(f"Nodo{i + 1}=seguidor{a}\n")
                a += 1
            else:
                archivo.write(f"Nodo{i + 1}=apagado\n")

# Monitoreo continuo
while True:
    escribir_estado()
    time.sleep(5)  # Puedes ajustar el intervalo de monitoreo según tus necesidades

