import pyautogui
import time

def limitar_movimento_mouse():
    print("Limitando movimento do mouse...")
    # Definição de limites para a área do mouse
    limit_x1, limit_y1 = 100, 100
    limit_x2, limit_y2 = 600, 600
    
    try:
        while True:
            # Posição Atual
            x, y = pyautogui.position()

            # Verifica os limites
            if x < limit_x1:
                x = limit_x1
            if y < limit_y1:
                y = limit_y1
            if x > limit_x2:
                x = limit_x2
            if y > limit_y2:
                y = limit_y2

            # Move se não tiver limitação
            pyautogui.moveTo(x, y)

            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Execução interrompida pelo usuário.")

limitar_movimento_mouse()
