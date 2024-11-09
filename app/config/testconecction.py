import pymysql

# Datos de conexión (reemplaza con los valores de tu base de datos Railway)
host = 'autorack.proxy.rlwy.net' #'mysql-u-ng.railway.internal'        # Dirección de tu host
user = 'root'     # Tu usuario de MySQL
password = 'dbLnhTjzsETZAlKEBfKoVFeCJfKsiDUw'  # Contraseña de tu usuario
database = 'railway' # Nombre de tu base de datos
port = 50812 #3306             # Cambia el puerto si es necesario


try:
    # Establecer conexión
    print("iniciando try")
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port
    )
    print("Conexión exitosa a la base de datos.")
except pymysql.MySQLError as e:
    print(f"Error al conectar a MySQL: {e}")
finally:
    # Cerrar conexión si está activa
    if connection and connection.open:
        connection.close()
        print("Conexión cerrada.")