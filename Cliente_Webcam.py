import cv2
import socket
import pickle
import struct

# Configurações do servidor
HOST = 'localhost'
PORT = 5000

# Inicializar captura de vídeo da webcam
cap = cv2.VideoCapture(0)

# Inicializar o socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print("Conectado ao servidor para transmissão de vídeo.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Codificar o quadro de vídeo como uma sequência de bytes
    data = pickle.dumps(frame)
    message = struct.pack("Q", len(data)) + data

    # Enviar o quadro para o servidor
    client_socket.sendall(message)

cap.release()
client_socket.close()
