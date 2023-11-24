import pika

class Conexion():
    """   
    Atributos:
        user: Usuario del servidor de RabbitMQ
        password: Contraseña del servicio
        server: IP del servidor
        port: Puerto de escucha de la cola 
        virtual_host: Host de rabbitMQ
        queue: Cola del proyecto
    """
    user = "admin"
    password = "admin"
    server = "10.10.1.123"
    port = 5672
    virtual_host = "/"
    queue = 'Forms_queue'
    
    def __init__(self):
        credential = pika.PlainCredentials(self.user, self.password)
        parameters = pika.ConnectionParameters(self.server, self.port, virtual_host=self.virtual_host ,credentials = credential)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue)        

    def send(self, message):
        self.channel.basic_publish(exchange='', routing_key=self.queue, body=message)

    def consuming(self, callback):
        self.channel.basic_consume(queue= self.queue , on_message_callback=callback, auto_ack=False)
        self.channel.start_consuming()

    def close(self):
        self.connection.close()

