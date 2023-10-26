import socket
import time

# Configurações do cliente
HOST = '127.0.0.1'
PORT = 12345

# Função para receber e salvar o conteúdo do arquivo
def receive_and_save_file():
    file_content = client_socket.recv(1024)
    with open('arquivo_recebido.txt', 'wb') as file:
        file.write(file_content)

# Inicialize o cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    # Receba o conteúdo do arquivo a cada 5 segundos (você pode ajustar o intervalo)
    receive_and_save_file()
    time.sleep(5)  # Aguarda 5 segundos antes de verificar novamente
