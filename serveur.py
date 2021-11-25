#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

def Main():
	host = "" # Entrez votre Ip ou hostname
	port = 5000
	co_princ = socket.socket() # 1. Créer un socket
	co_princ.bind((host, port)) # 2. Liaison du socket avec une adresse 
	co_princ.listen(1) # 3. Écoute du socket
	co_client, info_client = co_princ.accept() # 4. Établissement de la connexion
	print("Le serveur est connecté sur le port : "+str(info_client))

	# 5. Dialogue avec le client
	while True:
		data = co_client.recv(1024).decode('utf-8') # Reçoit le message du client en UTF-8
		if not data:
			break
		print("Le client vous envoie : "+data)
		co_client.send('Message envoye')
		data.encode('utf-8')

	# 6. Fermeture de la connexion   
	print("Fermeture de la connexion")
	co_princ.close()

if __name__ == '__main__':
    Main()
