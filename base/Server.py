import socket
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configurações do servidor
HOST = '127.0.0.1'
PORT = 12345

# Mantenha o conteúdo atual do arquivo
file_content = b""  # Inicialize como uma sequência de bytes vazia

# Classe para lidar com alterações no arquivo
class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        global file_content
        with open('arquivo.txt', 'rb') as file:
            file_content = file.read()
        for client_socket in clients:
            client_socket.send(file_content)

# Inicialize o servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Servidor escutando em {HOST}:{PORT}")

# Crie um observador de sistema de arquivos
file_observer = Observer()
file_observer.schedule(FileChangeHandler(), '.')

# Inicie o observador
file_observer.start()

# Mantenha uma lista de clientes
clients = []

while True:
    client_socket, addr = server_socket.accept()
    clients.append(client_socket)
    print(f"Conexão recebida de {addr}")
    client_socket.send(file_content)

# Encerre o observador quando você encerrar o servidor
file_observer.stop()
file_observer.join()
