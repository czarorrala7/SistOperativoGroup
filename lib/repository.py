import json
import os
import pickle


class Repository:
    """
    Clase de almacenamiento de datos o base de datos del producto.
    Administra los archivos .db y dbx (indice de la base)

    Métodos:
        get_index(): Si existe abre el archivo dbx y lo envia a memoria para el acceso rapido a la data
        set_data(data): Envia a la instancia la data a guardar
        save_data(partitions): Almacena la información en los archivos db y actualiza el indice en memoria
        save_index(partitions): Guarda el indice de memoria a disco (idx)
        read_data(user_id, partitions): En consultas, este lee el dato que se necesita, por clave (user_id)
        regenerate_index(partitions): En caso de daño del indice, esta funcion lee todos los db y crea un nuevo indice.
    """

    def get_index(self):
        if os.path.exists('./database/index.dbx'):
            with open("./database/index.dbx", "rb") as f:
                return pickle.load(f)
        else:
            return {}

    def set_data(self, data):
        for key, value in data.items():
            self.user_id = value['informacion_personal']['user_id']
        #self.user_id = data['user_id']
        self.data = data
        self.file_id = int(self.user_id[-1])
        self.filename = f"./database/data_{self.file_id}.db"
        
    def save_data(self, partitions):
        try:
            if self.user_id in partitions:
                print(f'User con problemas {self.user_id}')
                print(partitions)
                return 1
            try:
                file_position = os.path.getsize(self.filename)
            except FileNotFoundError:
                file_position = 0
                #print('Problema con el FileNotFoundError')
            with open(self.filename, "ab") as f:
                pickle.dump(self.data, f)
                data_position = f.tell()
            partitions[self.user_id] = {"filename": self.filename, "position": file_position, "size": data_position - file_position}
            return 1
        except Exception as ex:
            print('Error al grabar: ' + str(ex))
            return 0

    def save_index(self, partitions):
        with open('./database/index.dbx', 'wb') as f:
            pickle.dump(partitions, f)

    def read_data(self, user_id, partitions):
        if user_id not in partitions:
            return None
        else:
            print(partitions[user_id])
        filename = partitions[user_id]['filename']
        position = partitions[user_id]["position"]
        with open(filename, "rb") as f:
            f.seek(position)
            data = pickle.load(f)
        return data
    
    def regenerate_index(self, partitions):
        partitions.clear()
        for filename in os.listdir('./database'):
            print(filename)
            if filename.startswith("data_") and filename.endswith(".db"):
                partition_id = int(filename.split("_")[1].split(".")[0])
                with open('./database/'+filename, "rb") as f:
                    while True:
                        try:
                            data = pickle.load(f)
                            user_id = data["user_id"]
                            file_position = f.tell() - len(pickle.dumps(data))
                            partitions[user_id] = {"filename": filename, "position": file_position, "size": len(pickle.dumps(data))}
                        except EOFError:
                            break
        with open('./database/index.dbx', 'wb') as f:
            pickle.dump(partitions, f)




