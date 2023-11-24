from lib.db import Data
import uuid
import json

class Formulario():
    """
    Generacion de datos almacenados en un diccionario para ser llevados a RabbitMQ y posteriormente a un archivo.

    """

    def __init__(self):
        self.identificador = str(uuid.uuid4())
        self.data = Data()
        self.crear_formulario()

    def crear_formulario(self):
        genero = self.data.get_genero()
        self.informacion_persona = {
            self.identificador: {
             
                    "id": self.data.get_identificador_pasaporte(),
                    "nombre": self.data.get_nombres(genero),
                    "nacionalidad": self.data.get_lugarnacimiento(),
                    "cedula": self.data.get_cedula(),
                    "dirreccion": self.data.get_lugarnacimiento(),
                    "telefono": self.data.get_Telefono(),
                    "correo": self.data.get_correo(),
           
            }
        }
        
    def formulario_to_json(self):
        return json.dumps(self.informacion_persona)
