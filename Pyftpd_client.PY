#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from ftplib import FTP
import ftplib

# Authentification : 
user = input("-> Veuillez entrez votre nom d'utilisateur : ")
passwd = input("--> Veuillez entrez votre mot de passe : ")
print('\n')

def main():
	ftp = FTP('') # Nom de votre FTP 
	ftp.connect('ip_addr',2121) # Adresse IP ou Hostname ; port 
	ftp.login(user, passwd) # user : python-ftp ; passwd : test4
	ftp.cwd('Python3vsPython2') # Nom du dossier qui est dans le serveur FTP
	ftp.retrlines('LIST') # Pour lister tous les fichiers contenues dans le dossier
	print('\n')

	message = input("-> ") 
	while message != 'q':
		# Extraction des fichiers :
		if message == 1 : 
			ext_fichier = input("---> Nom du fichier à extraire: ")
			localfile = open(ext_fichier, 'wb')
			ftp.retrbinary('RETR ' + ext_fichier, localfile.write, 1024)
			localfile.close()
			ftp.quit()
		# Stockage des fichiers :	
		if message == 2 : 
			stok_fichier = input("---> Nom du fichier à stocker: ")
			ftp.storbinary('STOR '+stok_fichier, open(stok_fichier, 'rb'))
			ftp.quit()
		# Pour quitter le serveur :
		if message == 'q':
			ftp.quit()

if __name__ == '__main__':
    main()
