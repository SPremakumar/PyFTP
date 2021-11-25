#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import time

def Main():
	host = socket.gethostname()
	port = 5000
	co_serveur = socket.socket()
	co_serveur.connect((host, port))
	temps = int(time.strftime('%H'))   
	message = input("-> ")
	while message != 'q':
		co_serveur.send(message.encode('utf-8'))
		data = co_serveur.recv(1024).decode('utf-8')
		if 'bonjour'.lower() or 'salut'.lower() in message :
			if temps < 12 : 
				print('Bonjour')
			elif temps == 12 : 
				print('Bon appétit')
			elif temps > 12 : 
				print('Bon après-midi')
			elif temps > 17 :
				print('Bonsoir')
			else :
				print('Dites Bonjour')
		message = input("->")
	co_serveur.close()

if __name__ == '__main__':
    Main()
