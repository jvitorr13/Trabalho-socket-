import ctypes
import time

def desligar_monitor():
    """
    Desliga o monitor usando a API do Windows.
    """
    ctypes.windll.user32.SendMessageW(0xFFFF, 0x112, 0xF170, 2)

def ligar_monitor():
    """
    Religa o monitor movendo o mouse virtualmente.
    """
    ctypes.windll.user32.mouse_event(0x0001, 0, 0, 0, 0)

if __name__ == "__main__":
    print("Desligando o monitor em 3 segundos...")
    time.sleep(3)
    desligar_monitor()
    print("Monitor desligado! Pressione qualquer tecla ou mova o mouse para religar.")
