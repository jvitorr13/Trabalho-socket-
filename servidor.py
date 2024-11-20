import socket
import threading
import cv2
import pickle
import struct
import ctypes

# Configurações do servidor
HOST = 'localhost'
PORT = 5000
clientes = []       # Lista para armazenar clientes conectados
clientes_lock = threading.Lock()  # Lock para gerenciar a lista de clientes

# Função para desligar o monitor
def desligar_monitor():
    """
    Desliga o monitor usando a API do Windows.
    """
    ctypes.windll.user32.SendMessageW(0xFFFF, 0x112, 0xF170, 2)

# Função para lidar com mensagens de texto dos clientes
def tratar_cliente(cliente_socket, addr):
    print(f"Cliente conectado: {addr}")
    with clientes_lock:
        clientes.append(cliente_socket)  # Adiciona o cliente à lista de conexões

    try:
        while True:
            mensagem = cliente_socket.recv(1024).decode('utf-8')
            if not mensagem:  # Desconecta se a mensagem estiver vazia
                break
            print(f"Mensagem de {addr}: {mensagem}")

            # Verifica comandos específicos
            if mensagem.strip() == "/desligar_monitor":
                print("Comando recebido: Desligar monitor")
                desligar_monitor()
                cliente_socket.send("Monitor desligado com sucesso!".encode('utf-8'))
            else:
                transmitir_texto(mensagem, cliente_socket)  # Transmite para outros clientes
    except:
        pass
    finally:
        with clientes_lock:
            clientes.remove(cliente_socket)  # Remove o cliente ao desconectar
        cliente_socket.close()
        print(f"Cliente desconectado: {addr}")

# Função para transmitir mensagens de texto para todos os clientes conectados
def transmitir_texto(mensagem, remetente_socket):
    with clientes_lock:
        for cliente in clientes:
            if cliente != remetente_socket:  # Não envia de volta ao remetente
                try:
                    cliente.send(mensagem.encode('utf-8'))
                except:
                    cliente.close()
                    clientes.remove(cliente)

# Função para transmitir frames da webcam para os clientes
def webcam_stream():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Erro ao acessar a webcam.")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Serializa o frame para enviar pela rede
        data = pickle.dumps(frame)
        message = struct.pack("Q", len(data)) + data

        with clientes_lock:
            for cliente in clientes:
                try:
                    cliente.sendall(message)
                except:
                    clientes.remove(cliente)

    cap.release()
    print("Transmissão de vídeo encerrada.")

# Função para iniciar o servidor
def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen(5)
    print(f"Servidor rodando em {HOST}:{PORT}")

    # Thread separada para transmissão de vídeo
    webcam_thread = threading.Thread(target=webcam_stream)
    webcam_thread.start()

    try:
        while True:
            cliente_socket, addr = servidor.accept()  # Aceita conexão de um cliente
            print(f"Conexão aceita de {addr}")
            cliente_socket.send("Bem-vindo ao servidor! Use /desligar_monitor para desligar o monitor.".encode('utf-8'))

            # Cria uma thread para lidar com mensagens de texto do cliente
            thread = threading.Thread(target=tratar_cliente, args=(cliente_socket, addr))
            thread.start()
    except KeyboardInterrupt:
        print("\nServidor encerrado.")
    finally:
        servidor.close()

# Inicia o servidor
if __name__ == "__main__":
    iniciar_servidor()
