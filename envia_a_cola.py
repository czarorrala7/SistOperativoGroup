import pika
import os
import json

def enviar_a_rabbit(mensaje):
    # Conexión con el servidor RabbitMQ
    credentials = pika.PlainCredentials('admin', 'admin')
    parameters = pika.ConnectionParameters('192.168.100.134', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    # Declarar una cola (si no existe)
    channel.queue_declare(queue='Monitor')

    # Publicar el mensaje en la cola
    channel.basic_publish(exchange='', routing_key='Monitor', body=mensaje)

    print(f" [x] Enviado '{mensaje}' a la cola")

    # Cerrar la conexión
    connection.close()

def leer_json_y_enviar():
    # Nombre del archivo de salida
    nombre_archivo = 'salida.json'

    # Leer el contenido del archivo JSON
    with open(nombre_archivo, 'r') as archivo:
        contenido_json = json.load(archivo)

    # Convertir el contenido a cadena JSON
    contenido_str = json.dumps(contenido_json)

    # Enviar el contenido a la cola de RabbitMQ
    enviar_a_rabbit(contenido_str)

    # Eliminar el archivo de salida
    os.remove(nombre_archivo)
    print(f" [x] Archivo '{nombre_archivo}' eliminado")

if __name__ == '__main__':
    leer_json_y_enviar()
