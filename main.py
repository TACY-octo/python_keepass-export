# Function : Export keepass user. 
# Author   : Cyril TAVIAN
# Date     : 06/01/2020
# Gitlab   : https://github.com/ctavian/python_keepass-expor
# Version  : v0.2

import sys
from getpass import getpass
from pykeepass import PyKeePass

def init_keepass():
    '''
        Init keepass database
    '''

    try: 
        '''
            the inputs for  keepass database file. 
        '''
        keepass_path = input('Chemin du fichier keepass : ')
        keepass_password = getpass(prompt='Mot de passse du fichier keepass : ', stream=None)
        keepass_database = PyKeePass(keepass_path, password=keepass_password)
    except: 
        print('Problème de fichier ou de mot de passe !')
        exit(1)

    return keepass_database


def export_keepass(keepass_database):
    '''
        Export keepass_table to file.
    '''
    try:
        '''
            Input variable. 
        '''
        list_user = []
        keepass_table = []
        keepass_nb_user = input('Nombre de compte à rechercher ? : ')

        '''
            Create a user list for research in keepass_database. 
        '''
        nb_user = 0
        while nb_user < int(keepass_nb_user): 
            user_to_add = input('Le nom de l\'utilisateur à rechercher ? : ')
            list_user.append(user_to_add)
            nb_user += 1 

        '''
            Loop for search and add to list keepass_table.
        '''
        for n in list_user:
            user = keepass_database.find_entries(username=n) 
            for i in user: 
                if not any(d['password'] == i.password for d in keepass_table):
                    keepass_table.append({'id' : i.title, 'login' : i.username, 'password' : i.password, 'config' : i.title})

        '''
            Create export file 
        '''
        with open('keepass_export', "w") as fichier: 
            for a in keepass_table: 
                fichier.write(str(a) +",\n")    
    except: 
        print('Une erreur est survenue lors de l\'export')

def main():
    export_keepass(init_keepass())

main()
