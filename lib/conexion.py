import pika

class Conexion():
    """
   Esta clase se encarga de administrar RabbitMQ en el proyecto, supervisando tanto la conexión como el envío y consumo de datos en la cola.

Atributos:

    user: Nombre de usuario del servidor RabbitMQ.
    password: Contraseña del servicio.
    server: Dirección IP del servidor.
    port: Puerto de escucha de la cola.
    virtual_host: Host de RabbitMQ.
    queue: Cola específica del proyecto.

Métodos:

    __init__(): Inicializa la clase con los parámetros del módulo.
    def_send(message): Envía el mensaje a la cola.
    def_consuming(callback): Captura cada mensaje que ingresa a la cola, asegurando su entrega mediante el control proporcionado por la función de devolución de llamada.
    """
    user = "admin"
    password = "admin"
    server = "10.10.1.104"
    port = 5672
    virtual_host = "/"
    queue = 'Forms_queue'
    
    def __init__(self):
        credential = pika.PlainCredentials(self.user, self.password)
        parameters = pika.ConnectionParameters(self.server, self.port, virtual_host=self.virtual_host ,credentials = credential)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
        #declarar la cola de rabiitMQ
        self.channel.queue_declare(queue=self.queue, passive=False, durable=True, exclusive=False, auto_delete=False, arguments=None)
        #self.channel.queue_declare(queue=self.queue)

    def send(self, message):
        self.channel.basic_publish(exchange='', routing_key=self.queue, body=message)

    def consuming(self, callback):
        self.channel.basic_consume(queue= self.queue , on_message_callback=callback, auto_ack=False)
        self.channel.start_consuming()

    def close(self):
        self.connection.close()

