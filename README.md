# python_keepass-export

``` Version : 0.2 ``` 

# Besoin 
Exporter un ou plusieurs comptes d'un fichier Keepass dans un fichier export sous une forme d'item dict.  

# Prérequis 
Avoir installer le module ``` PyKeePass ``` 
```
pip install PyKeePass
```

# Utilisation 
Executer le script python et renseigner la valeur à chaque demande. 
- Chemin du fichier keepass : (Chemin du fichier keepass). 
- Mot de passse du fichier keepass : (Mot de passe du fichier keepass).
- Nombre de compte à rechercher ? : (Nombre d'utilisateur à rechercher ex: 5).
- Le nom de l'utilisateur à rechercher ? : (renseigner le nom de l'utilisateur ex: master). 
-> Cette question va être joué pour incrémenter une liste de nom d'utilisateur. Vous définissez le nombre de tour à la question "Nombre de compte à rechercher". 

Une fois le script exécuté, vous trouverez un fichier nommé "keepass_export". 

# Composition 

## Fonction init_keepass 

Elle permet de retourner un objet "keepass_database". 

## Fonction export_keepass

Elle permet de rechercher une liste d'utilisateur et de les écricres dans un fichier keepass_export. 

## Fonction main

Lance les deux fonctions précédentes. 
