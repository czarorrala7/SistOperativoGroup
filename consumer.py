import pika
import json
import os

def callback(ch, method, properties, body):
    try:
        # Leer el archivo de configuración
        with open('configuracion.json', 'r') as config_file:
            configuracion = json.load(config_file)

        # Encontrar el nodo con cargo "lider"
        lider = next((nodo for nodo in configuracion if nodo["rol"] == "lider"), None)

        if lider:
            # Obtener el nombre de la carpeta del nodo líder
            carpeta_lider = lider["nodo"]

            # Crear la carpeta si no existe
            if not os.path.exists(carpeta_lider):
                os.makedirs(carpeta_lider)

            # Decodificar el cuerpo del mensaje como JSON
            mensaje_json = json.loads(body.decode('utf-8'))

            # Obtener la ruta completa del archivo dataBase.json en la carpeta del líder
            ruta_archivo = os.path.join(carpeta_lider, 'dataBase.json')

            # Inicializar la lista de datos existente
            datos_existente = []

            # Leer el contenido actual del archivo si existe
            if os.path.exists(ruta_archivo):
                try:
                    with open(ruta_archivo, 'r') as archivo_existente:
                        datos_existente = json.load(archivo_existente)
                except (FileNotFoundError, json.JSONDecodeError):
                    # Si hay algún error al cargar, simplemente mantener la lista vacía
                    pass

            # Unir las listas existentes y el nuevo mensaje
            datos_totales = datos_existente + mensaje_json
            
            # Escribir todos los datos en el nuevo archivo
            with open(ruta_archivo, 'w') as archivo:
                # Escribir la lista de datos_totales como una lista de objetos JSON
                json.dump(datos_totales, archivo, indent=2)

    except json.JSONDecodeError as e:
        print("Error al decodificar el mensaje JSON:", str(e))

def leer_cola_y_consolidar():
    # Conexión con el servidor RabbitMQ
    credentials = pika.PlainCredentials('michael', 'michael')
    parameters = pika.ConnectionParameters('192.168.100.134', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    # Declarar la cola desde la que leeremos mensajes
    channel.queue_declare(queue='Monitor')  # No forzamos la propiedad 'durable'

    # Configurar el callback para procesar los mensajes
    channel.basic_consume(queue='Monitor', on_message_callback=callback, auto_ack=True)

    print(' [*] Esperando mensajes. Presiona CTRL+C para salir.')

    try:
        # Iniciar la recepción de mensajes
        channel.start_consuming()
    except KeyboardInterrupt:
        pass
    finally:
        # Cerrar la conexión al servidor RabbitMQ
        connection.close()

if __name__ == '__main__':
    leer_cola_y_consolidar()
