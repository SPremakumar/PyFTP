#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user('python-ftp', 'test4', '/home/python-ftp', perm='elradfmwMT') # nom utilisateur; mot de passe; chemin du répertoire voulu dans le serveur FTP ; et les permissions (lecture et écriture)
    # POUR RENDRE LE SERVEUR FTP ANONYME : User = 'anonymous', passwd = ''
    # authorizer.add_anonymous('/home/python-ftp', perm='elradfmwMT')
    
    handler = FTPHandler
    handler.banner = "Bienvenue dans Pyftpd-serveur" # Bannière
    handler.masquerade_address = "spremakumar.ddns.net" # DOMAINE ou IP
    handler.passive_ports = range(60000, 65535) # Passive mode 
    address = ('ip', 2121) # Entrez votre Ip adresse
    server = FTPServer(address, handler)
    server.max_cons = 256
    server.max_cons_per_ip = 5
    server.serve_forever()
    
if __name__ == '__main__':
    main()	
