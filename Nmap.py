import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse

NUM_THREADS = 50

target_url = input('㊦ | Введите целевой IP/САЙТ/Digite o IP/SITE alvo: ')
parsed_url = urlparse(target_url)
target_host = parsed_url.netloc.split(':')[0]  # Extrai o nome do host da URL
port_range = range(1, 8080)  # Esta faixa de porta pode ser alterada pelo usuário

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target_host, port))
    sock.close()
    return port, result == 0

open_ports = []

with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
    futures = [executor.submit(scan_port, port) for port in port_range]
    num_scanned = 0
    for future in as_completed(futures):
        num_scanned += 1
        port, is_open = future.result()
        if is_open:
            open_ports.append(port)
        print(f"\rпорт сканирования/Escaneando porta {port} de {len(port_range)}", end="")

print("\nPortas abertas:")
for port in open_ports:
    print(port)

input('Нажмите Enter, чтобы выйти. Сделано Noutz/Aperte enter para sair Feito por Noutz . ')
