from lib.repository import Repository

# Instanciar la clase Repository
db = Repository()

# Obtener el índice
indice = db.get_index()

# Imprimir los datos leídos
print(db.read_data('identificador', indice))
