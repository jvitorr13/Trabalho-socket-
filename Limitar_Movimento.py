import pyautogui
import time

def limitar_movimento_mouse():
    print("Limitando movimento do mouse...")
    # Defina os limites para a área do mouse (exemplo: uma caixa de 500x500 pixels)
    limit_x1, limit_y1 = 100, 100
    limit_x2, limit_y2 = 600, 600
    
    try:
        while True:
            # Obtém a posição atual do mouse
            x, y = pyautogui.position()

            # Verifica se o mouse ultrapassou os limites e move de volta
            if x < limit_x1:
                x = limit_x1
            if y < limit_y1:
                y = limit_y1
            if x > limit_x2:
                x = limit_x2
            if y > limit_y2:
                y = limit_y2

            # Se o mouse não estiver no limite, move-o
            pyautogui.moveTo(x, y)

            # Atraso para evitar uso excessivo da CPU
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Execução interrompida pelo usuário.")

# Chame a função para testar
limitar_movimento_mouse()
