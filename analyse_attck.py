import psutil

# Obtenir les informations sur l'utilisation du réseau par les processus
network_connections = psutil.net_connections(kind='inet')

# Parcourir les connexions réseau pour identifier les processus suspect
for conn in network_connections:
    if conn.status == 'ESTABLISHED' and conn.pid:
        process = psutil.Process(conn.pid)
        if process.name() not in ['System', 'Idle']:
            print(f"Processus suspect : {process.name()} (PID : {conn.pid}) utilise l'adresse IP locale {conn.laddr.ip} et le port {conn.laddr.port} pour communiquer avec l'adresse IP distante {conn.raddr.ip} et le port {conn.raddr.port}")