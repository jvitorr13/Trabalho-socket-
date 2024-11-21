import pyautogui
import time

def inverter_mouse():
    largura_tela, altura_tela = pyautogui.size()
    print("Inversão do movimento do mouse ativada!")
    
    try:
        while True:
            # posição atual do mouse
            x, y = pyautogui.position()

            # Calcula a posição invertida
            x_invertido = largura_tela - x
            y_invertido = altura_tela - y

            # Move para a nova posição
            pyautogui.moveTo(x_invertido, y_invertido)
            time.sleep(0.01)  # Ajusta o delay para controlar a velocidade
    except KeyboardInterrupt:
        print("Inversão desativada.")

if __name__ == "__main__":
    inverter_mouse()
