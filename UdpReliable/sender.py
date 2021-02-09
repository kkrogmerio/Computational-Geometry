# emitator Reliable UDP
from helper import *
from argparse import ArgumentParser
import socket
import logging
import sys
from traceback import *
logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

def connect(sock, adresa_receptor):


    window=0
    seq_nr = 100
    flags = 'S'
    checksum = 0
    wel=''#acest wel e degeaba..
    octeti_header_fara_checksum = create_header_emitator(seq_nr, checksum,flags)
    
    mesaj = octeti_header_fara_checksum 

    checksum = calculeaza_checksum(mesaj)

    octeti_header_cu_checksum = create_header_emitator(seq_nr, checksum,flags)
    
    mesaj = octeti_header_cu_checksum 

    
    sock.sendto(mesaj, adresa_receptor)

    
    connectionOk=1
    while True:
        connectionOk=1
        try:
            data, server = sock.recvfrom(MAX_SEGMENT)
        except socket.timeout as e:
            logging.info("Timeout la connect, retrying...")
            connectionOk=0
        if connectionOk==1:
            break
    
    if verifica_checksum(data) is False:

        return -1, -1
    
    ack_nr, checksum, window = parse_header_receptor(data)

    logging.info('Ack Nr: "%d"', ack_nr)
    logging.info('Checksum: "%d"', checksum)
    logging.info('Window: "%d"', window)
    
    return ack_nr, window


def finalize(sock, adresa_receptor, seq_nr):

    flags='F'

    checksum = 0
    octeti_header_cu_checksum = create_header_emitator(seq_nr, checksum,flags)

    mesaj = octeti_header_cu_checksum 

    checksum = calculeaza_checksum(mesaj)

    octeti_header_cu_checksum = create_header_emitator(seq_nr, checksum,flags)
    
    mesaj = octeti_header_cu_checksum 
    sock.sendto(mesaj, adresa_receptor)
    connectionOk=1


    while True:
        connectionOk=1
        try:
            data, server = sock.recvfrom(MAX_SEGMENT)
        except socket.timeout as e:
            logging.info("Timeout la connect, retrying...")
            connectionOk=0
        if connectionOk==1:
            break

    if verifica_checksum(data) is False:

        return -1, -1
    
    ack_nr, checksum, window = parse_header_receptor(data)

    logging.info('Ack Nr: "%d"', ack_nr)
    logging.info('Checksum: "%d"', checksum)
    logging.info('Window: "%d"', window)

    return 0  

def send(sock, adresa_receptor, seq_nr, window, octeti_payload):
    '''
    Functie care trimite octeti ca payload catre receptor
    cu seq_nr dat ca parametru.
    Returneaza ack_nr si window curent primit de la server.
    '''

    checksum=0
    flag='P'
    header=create_header_emitator(seq_nr+1,0,flag,octeti_payload)
    checksum = calculeaza_checksum(header)

    header=create_header_emitator(seq_nr+1,checksum,flag,octeti_payload)

    sock.sendto(header,adresa_receptor)

    connectionOk=1

    while True:
        connectionOk=1
        try:
            data, server = sock.recvfrom(MAX_SEGMENT)
        except socket.timeout as e:
            logging.info("Timeout la connect, retrying...")
            connectionOk=0
        if connectionOk==1:
            break

    if verifica_checksum(data) is False:
        return -1, -1
    
    ack_nr, checksum, window = parse_header_receptor(data)
    logging.info('Ack Nr: "%d"', ack_nr)
    logging.info('Checksum: "%d"', checksum)
    logging.info('Window: "%d"', window)
    return ack_nr, window
import os

def main():
    parser = ArgumentParser(usage=__file__ + ' '
                                             '-a/--adresa IP '
                                             '-p/--port PORT'
                                             '-f/--fisier FILE_PATH',
                            description='Reliable UDP Emitter')

    parser.add_argument('-a', '--adresa',
                        dest='adresa',
                        default='receptor',
                        help='Adresa IP a receptorului (IP-ul containerului, localhost sau altceva)')

    parser.add_argument('-p', '--port',
                        dest='port',
                        default='10000',
                        help='Portul pe care asculta receptorul pentru mesaje')

    parser.add_argument('-f', '--fisier',
                        dest='fisier',
                        help='Calea catre fisierul care urmeaza a fi trimis')

    args = vars(parser.parse_args())

    ip_receptor = args['adresa']
    port_receptor = args['port']
    fisier = args['fisier']
    fisEmitator=fisier
    adresa_receptor = (ip_receptor, int(port_receptor))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP)

    filed=open(fisier,'rb')
    sock.settimeout(3)

    file_descriptor = open(fisier, 'rb')
    ack_nr, window = connect(sock, adresa_receptor)
    send_seq_nr = ack_nr
    segment=citeste_segment(file_descriptor)

    while True:
        try:

            if window!=1:
                continue

            try:
                payload_segment = next(segment)
            except StopIteration:
                break
            send_seq_nr, window = send(sock, adresa_receptor, send_seq_nr, window, payload_segment)

        except Exception:

            sock.close()
            file_descriptor.close()
    
    finalize(sock, adresa_receptor,send_seq_nr)



if __name__ == '__main__':
    main()