import psutil
import time

while True:
    # Récupérer l'utilisation du CPU en pourcentage
    cpu_percent = psutil.cpu_percent()
    
    # Récupérer l'utilisation de la mémoire en octets
    memory_usage = psutil.virtual_memory().used
    
    # Récupérer l'utilisation du disque en octets
    disk_usage = psutil.disk_usage('/').used
    
    # Afficher les informations système
    print(f"CPU: {cpu_percent}%  Mémoire: {memory_usage} octets  Disque: {disk_usage} octets")
    
    # Attendre 5 secondes avant de continuer
    time.sleep(5)
