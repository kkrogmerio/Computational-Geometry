import struct
import socket
import logging

MAX_UINT32 = 0xFFFFFFFF
MAX_BITI_CHECKSUM = 16
MAX_SEGMENT = 1400

def compara_endianness(numar):

    print ("Numarul: ", numar)
    print ("Network Order (Big Endian): ", [bin(byte) for byte in struct.pack('!H', numar)])
    print ("Little Endian: ", [bin(byte) for byte in struct.pack('<H', numar)])

fisEmitator=None
def create_header_emitator(seq_nr, checksum,flags='S',payload=b'',wel='No message'):

    spf_zero=None   
    if flags=='S':
        spf = 0b100 
        spf_zero = spf << 13

    elif flags=='P':
        spf = 0b010 
        spf_zero = spf << 13

    elif flags=='F':
        spf = 0b001
        spf_zero = spf << 13
    print("SEQ NR=",seq_nr,"CHECKSUM=",checksum,"SPF_ZERO=",spf_zero)
    octeti = struct.pack('!LHH', seq_nr, checksum,spf_zero)

    octeti+=payload

    return octeti


def parse_header_emitator(octeti):

    seq_nr, checksum, spf= struct.unpack('!LHH',octeti[:8])
    payload=octeti[8:]

    spf>>=13
    flags=""
    print(spf)
    if spf & 0b100:

        flags = 'S'
    elif spf & 0b001:

        flags = 'F'
    elif spf & 0b010:

        flags = 'P'
    print("DUPA FLAGS=",flags)
    return (seq_nr, checksum, flags,payload)


def create_header_receptor(ack_nr, checksum, window,NoUse=0):

    octeti = struct.pack('!LHH', ack_nr, checksum, window)
    return octeti


def parse_header_receptor(octeti):

    ack_nr, checksum, window= struct.unpack('!LHH',octeti)
    return (ack_nr, checksum, window)


def citeste_segment(file_descriptor):

    yield file_descriptor.read(MAX_SEGMENT)


def exemplu_citire(cale_catre_fisier):
    with open(cale_catre_fisier, 'rb') as file_in:
        for segment in citeste_segment(file_in):
            print(segment)


def calculeaza_checksum(octeti):
    checksum = 0
    print("octeti= ",octeti)
    if(len(octeti)%2!=0):
        octeti+=bytes([0])
    
    #print(len(octeti))
    seqnum1,seqnum2,checks,spf=struct.unpack('!HHHH',octeti[:8])
    payloads=octeti[8:]

    payload=struct.unpack('H'*int(len(payloads)/2),payloads)


    checksum=(checksum+seqnum1)%pow(2,16)
    checksum=(checksum+seqnum2)%pow(2,16)
    checksum=(checksum+checks)%pow(2,16)
    checksum=(checksum+spf)%pow(2,16) 
    for i in payload:
        checksum=(checksum+i) % pow(2,16)  
    checksum=~(-checksum)
    print("CHECKSUM===",checksum)

    return checksum


def verifica_checksum(octeti):
    if calculeaza_checksum(octeti):
        return True
    return False



if __name__ == '__main__':
    compara_endianness(16)