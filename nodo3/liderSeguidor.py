from flask import Flask, jsonify
import requests
import json
import threading
import time
import shutil
import os

lv_puerto = 5233
nodos_puertos = [
        {"nodo": "nodo1", "puerto": 5231},
        {"nodo": "nodo2", "puerto": 5232},
        {"nodo": "nodo3", "puerto": 5233},
        {"nodo": "nodo4", "puerto": 5234}
    ]
ln_band = 0
app = Flask(__name__)

def verificar_estado_nodo(url, puerto, nodo):
    global ln_band
    try:
        rol = "seguidor"
        response = requests.get(url)
        #puerto="{}".format(puerto)
        if response.status_code == 200:
            # Nodo está levantado
            if ln_band == 0:
                rol = "lider"
                ln_band += 1
            return {"nodo": nodo, "rol": rol, "url": url, "estado": "encendido", "puerto": puerto}
        else:
            # Nodo está apagado
            return {"nodo": nodo, "rol": rol, "url": url, "estado": "apagado", "puerto": puerto}
    except requests.exceptions.RequestException:
        # Nodo está apagado (no se puede conectar)
        return {"nodo": nodo, "rol": rol, "url": url, "estado": "apagado", "puerto": puerto}

def verificar_nodos_periodicamente():
    global ln_band    
    global lv_puerto
    while True:        
        configuracion = []
        lv_es_lider="N"
        ln_band = 0
        # Verificar el estado de los otros nodos
        for nodo_info in nodos_puertos:
            estado_nodos = verificar_estado_nodo(f"http://localhost:{nodo_info['puerto']}", nodo_info['puerto'], nodo_info['nodo'])
            configuracion.append(estado_nodos)
            if estado_nodos["puerto"] == lv_puerto and estado_nodos["rol"] == "lider":
                lv_es_lider="S"
                
        if lv_es_lider=="S":            
            with open('../configuracion.json', 'w') as archivo_config:
                json.dump(configuracion, archivo_config, indent=2)
        else:
            carpeta_lider = next((nodo["nodo"] for nodo in configuracion if nodo["rol"] == "lider"), None)
            
            ruta_dataBase_lider = os.path.join('..',carpeta_lider, "dataBase.json")
            print(ruta_dataBase_lider)
            carpeta_seguidor = next((nodo["nodo"] for nodo in configuracion if nodo["puerto"] == lv_puerto), None)
            ruta_dataBase_seguidor = os.path.join('..',carpeta_seguidor, "dataBase.json")
            #ruta_dataBase_seguidor = os.path.join('..',estado_nodos["nodo"], "dataBase.json")
            print(ruta_dataBase_seguidor)
            shutil.copy(ruta_dataBase_lider, ruta_dataBase_seguidor)
        time.sleep(5)  # Esperar 10 segundos antes de la siguiente verificación

# Iniciar el hilo para verificar nodos periódicamente
verificacion_thread = threading.Thread(target=verificar_nodos_periodicamente)
verificacion_thread.start()

@app.route('/')
def hello():
    return jsonify(message="¡Hola desde el nodo!" + str(lv_puerto) )

if __name__ == '__main__':
    app.run(port=lv_puerto)
