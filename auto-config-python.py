import getpass
import sys
import telnetlib

HOST = "192.168.1.1"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

f=open("cisco-config-python.txt","r")
f1=f.readlines()
for x in f1:
	tn.write(x)

print tn.read_all()
