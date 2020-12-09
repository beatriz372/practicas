   # Importamos las librerias
import socket
# Establecemos el tipo de socket/conexion
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5000 # Puerto de comunicacion
sock.bind(('127.0.0.1',9000)) # IP y Puerto de conexion en una Tupla

print ("ESPERANDO CONEXIONES EN EL PUERTO", 9000)

# Vamos a esperar que un cliente se conecte
sock.listen(1)

#La conexion que servira para enviar datos y recibir datos
con, client_addr =  sock.accept()
print("CLIENTE CONECTADO")
text = "Hola, soy el servidor" # El texto que enviaremos
con.send(text.encode()) # Enviamos el texto al cliente que se conecta

con.close() # Cerramos la conexion
sock.close() # Cerramos el socket
print ("CLIENTE DESCONECTADO")
