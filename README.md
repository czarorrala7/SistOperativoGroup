# SistOperativoGroup
El conjunto de arhivos esta distribuido asi:

1. Genera de forma alteatoria los formularios
2. envia_a_cola.py: Lanza en el servidor de generación de formularios el proceso de envio de los mismos a la cola RabbitMQ
3. obtiene_cola.py: Lanza el servidor de consumer de mensajes de la cola
4. apis: Lanza el crud para actualizar la informacion de la base
5. lidenseguidor.py: Proceso principal de ejecución en los nodos de sistema de almacenamiento, ademas de coordinación de instancias (lider - seguidor)


Dentro de la carpeta files:
Se encuentran los arhivos almacenados de formularios

pip install flask pika kazoo
 
.\rabbitmq-service.bat install
.\rabbitmq-service.bat enable       
.\rabbitmq-service.bat start
 
http://localhost:15672/
usr/pwd: admin/admin
Agregar cola Forms_queue                            
 
1.  Ejecutar genera.py
2.  Ejecutar envia_a_cola.py
3.  Ejecutar obtiene_cola.py
4.  Ejecutar lidenseguidor.py
5.  Ejectar api
 
