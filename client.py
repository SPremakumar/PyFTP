#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

def Main():
	host =  "" #Entrez votre adresse Ip ou hostname
	port = 5000
	co_serveur = socket.socket() # 1. Créer un socket
	co_serveur.connect((host, port)) # 2. Connexion du client avec le serveur

	message = input("-> ") # 3. Dialogue avec le serveur 
	while message != 'q':
		co_serveur.send(message.encode('utf-8'))
		data = co_serveur.recv(1024).decode('utf-8')
		if 'bonjour'.lower() in message.lower() :
			print('Bonsoir')
		else :
			print('Dites Bonjour')
		message = input("->")
	co_serveur.close() # 4. Fermeture de la connexion :

if __name__ == '__main__':
    Main()
