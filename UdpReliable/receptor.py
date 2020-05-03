# receptor Reiable UDP
from helper import *
from argparse import ArgumentParser
import socket
import logging
import random
from itertools import zip_longest
logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-10s [%(asctime)s]  %(message)s', level = logging.NOTSET)

def main():
    parser = ArgumentParser(usage=__file__ + ' '
                                             '-p/--port PORT'
                                             '-f/--fisier FILE_PATH',
                            description='Reliable UDP Receptor')

    parser.add_argument('-p', '--port',
                        dest='port',
                        default='10000',
                        help='Portul pe care sa porneasca receptorul pentru a primi mesaje')

    parser.add_argument('-f', '--fisier',
                        dest='fisier',
                        help='Calea catre fisierul in care se vor scrie octetii primiti')
    

    args = vars(parser.parse_args())
    port = int(args['port'])
    fisier = args['fisier']

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP)

    adresa = '0.0.0.0'
    server_address = (adresa, port)
    sock.bind(server_address)
    logging.info("Serverul a pornit pe %s si portnul portul %d", adresa, port)
    fout=open(fisier,'wb')
    while True:
        logging.info('Asteptam mesaje...')
        data, address = sock.recvfrom(MAX_SEGMENT)
        (seq_nr, checksum, flags,payload)=parse_header_emitator(data) 
        if seq_nr==None:
            continue
        print("INAUNTRUU SEQ NR=",seq_nr,"CHECKSUM=",checksum,"flag",flags,"payload=",payload)
        if verifica_checksum(create_header_emitator(seq_nr,checksum,flags,payload))==True:
            print('S-a primit cu succes mesajul')
        else:
            print('mesajul nu s-a primit corect')
            break

        if flags=='S':
            ack=seq_nr+1
        elif flags=='F':
            ack=seq_nr+1
            fout.close()
        elif flags=='P':
            ack=seq_nr
            fout.write(payload) 
        mesaj=create_header_receptor(ack,checksum,1)

        checksum=calculeaza_checksum(mesaj)
        mesajCuChecksum=create_header_receptor(ack,checksum,1)
        sock.sendto(mesajCuChecksum,address)
    
    frec=open(fisEmitator,'rb')

    with open(fisier, 'rb') as f1, open(fisEmitator, 'rb') as f2:
        for line1, line2 in zip_longest(f1, f2, fillvalue=None):
            if line1 == line2:
                continue
            else:
                print("Files aren't equally")
        print("Files are equally")
    fout.close()
    frec.close()



if __name__ == '__main__':
    main()

