# SistOperativoGroup
El conjunto de arhivos esta distribuido asi:

1. capture.py: Lanza en el servidor de generación de formularios el proceso de envio de los mismos a la cola RabbitMQ
2. consumer.py: Lanza el servidor de consumer de mensajes de la cola
3. apis.py: Lanza el servidor para el consumo de los archivos por medio del lider
4. main.py: Proceso principal de ejecución en los nodos de sistema de almacenamiento, ademas de coordinación de instancias (lider - seguidor)

Dentro de la carpeta lib se encuentran las clases motores de cada proceso:
1. conexion.py: Guarda la logica de la conexion con RabbitMQ
2. db.py: base de datos de posibles valores para los formularios
3. repository.py: Base de datos de almacenamiento de los formularios obtenidos
4. apis.py: Provee los archivos para que el nodo lider los consuma
5. zoo.py: Nodos de zookeeper entre los que se turna el liderato

Dentro de la carpeta files:
Se encuentran los arhivos almacenados de formularios

pip install flask pika kazoo
 
.\rabbitmq-service.bat install
.\rabbitmq-service.bat enable       
.\rabbitmq-service.bat start
 
http://localhost:15672/
usr/pwd: admin/admin
Agregar cola Forms_queue                            
 
1.  Ejecutar capture.py
2.  Ejecutar consumer.py
3.  Ejecutar apis.py
4.  Ejecutar main
5.  Ejectar analítica.py
 
