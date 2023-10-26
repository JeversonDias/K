import socket

# Configurações do cliente
HOST = '127.0.0.1'
PORT = 12345

# Inicialize o cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Função para receber e salvar o conteúdo do arquivo
def receive_and_save_file():
    file_content = client_socket.recv(1024)
    with open('arquivo_recebido.txt', 'wb') as file:
        file.write(file_content)

# Receba o conteúdo do arquivo uma vez ao se conectar
receive_and_save_file()

# Agora, você pode adicionar código para monitorar o arquivo ou interagir com o servidor
# para receber atualizações em tempo real, se necessário

client_socket.close()
