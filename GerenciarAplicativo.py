import subprocess
import sys

def instalar_e_executar(app_name):
    try:
        print(f"Instalando e executando {app_name}...")
        subprocess.call(["pip", "install", app_name])
        subprocess.call([app_name])
    except Exception as e:
        print(f"Erro ao instalar/rodar o aplicativo: {e}")

if __name__ == "__main__":
    app_name = sys.argv[1]
    instalar_e_executar(app_name)
