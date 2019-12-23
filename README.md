![alt text](https://img.shields.io/github/license/taurus-silver-17/Devops-ing4)
![alt text](https://img.shields.io/badge/Python-3.6-green "Logo Title Text 1")
![alt text](https://img.shields.io/badge/Docker%20Build-Passing-green)
![alt text](https://img.shields.io/badge/Docker%20Build%20-Automated-blue)
![alt text](https://img.shields.io/badge/Build-failure-red)
![alt text](https://img.shields.io/github/forks/taurus-silver-17/Devops-ing4)
![alt text](https://img.shields.io/github/repo-size/Taurus-silver-17/Devops-ing4)

# Devops's project during the 4th engineering 
By Arnaud Jullemier-Millasseau and Lilian Delaplace TD03 (inter)



# Table of contents
1. [Introduction](#introduction)
2. [Assignements](#assignements)
3. [The project](#theproject)
    1. [Docker](#docker)
    2. [Test](#test)
    3. [Licence](#licence)
    4. [Label](#label)
    5. [Who did what ?](#who)
        1. [Team](#team)
        2. [Task](#task)
4. [How to launch it](#nasa)

## This is the introduction <a name="introduction"></a>
The purpose of this directory is to respond to an homework of Devops. The goal is to put into practice the right methodology for a Devops project.
![alt text](https://github.com/taurus-silver-17/Devops-ing4/blob/master/static/img/devops.png)

## Requirements for this project <a name="assignements"></a>
 As a reminder, here are the notation criteria for the DEVOPS project:
- Use git, use branches, use tags
- Your project must have tests with a testing framework (depending on the language used)
- If you project uses external dependencies such as a database, use docker-compose to start it before the test session.
- Configure your project to use a CI server
- Provide a "README" file explaining how to launch your project, how to launch the tests, what problems your had

## The project <a name="theproject"></a>
We started from a project that Arnaud had already realized with a former colleague, this project is described and accessible in "the release v1.0". 

The goal of the project is to manage lights via a raspberry pi, we realized the same principle almost but this time with containers. We remind nevertheless that if the code doesn't work, the goal of this project is not a computer project but a Devops project. 



## Docker <a name="docker"></a>

il y a actuellement 3 conteneurs qui tournent : 
-devops-db qui est un conteneur postgre 
-devops-ci qui est le cotneneur sonarqube 
-Le conteneur devops-main qui contient l'application python et qui est une base du coteneur nginx Qui sont déployés via docker-compose lorsqu'on se connecte à l'adresse : "http://163.172.64.25:8080"

![alt text](https://github.com/taurus-silver-17/Devops-ing4/blob/master/static/img/schema_docker.png)

Ici on 4 fichiers : 
-docker-compose.yml : ici on déclare nos 3 services : 
-devops-db qui sera le premier conteneur pour la bdd, on lui donne un nom pour le DNS : devops-db. 

On donne ensuite des variables d'environnment pour la création de la bdd postgres 
-devops-ci qui est le 2ème conteneur, pour le serveur CI 
-devops-main : ici on ne précise pas d'image, puisqu'on va partir d'un docker file comme nous allons créer notre image à partir de nos fichiers. 

On retrouve nos variables d'environnments puisque ce sont des paramètres qui serviront dans nos fichiers de configuration "mettre image1" Donc nous pouvons ci-dessus, les variables d'environnments définis à la création du conteneur que l'on récupère dans l'application. 
Ensuite on définit le paramètre port qui permet la redirection du port 80 pour notre conteneur vers le port 8080 de la machine hôte. On déclare des dépendances, qui vont nous permettre de dire que si les conteneurs indiqués ne sont pas correctents démarrés, on arrête le build du conteneur en question. 
On a un paramètre build qui nous permet d'indiquer le chemin vers le docker file. Maintenant parlons du docker file : il permet de créer l'image du conteneur devops-main. On part d'un conteneur NGINX, on copie les fichiers dont on aura besoin plus tard (fichier de configuration et fichier entry-point). 
On exécute ensuite une série de commandes permettant la préparation et l'installation de nos dépendances logiciels. Après nous allons colner le projet Github à la racine du serveur web. 

Enfin nous éxécutons l'entry-point via la directive unique "CMD" ce qui nous renvoie à "l'entry point". L'entry point est le point d'entrée du conteneur c'est à dire : une ou plusieurs commandes à exécuter, une fois le contenueur créé sur la base de l'image construite, selon le docker file. 

Une fois qu'on dispose de tout ca on exécute : docker-compose build afin de construire l'architecture et les images selon la description fournit dans le fichier : docker-compose.yml

Enfin pour instancier les conteneurs, on exécute docker-compose up -d Les conteneurs seront détachés en tâche de fond : "image 2 "

Ici nous pouvons le résultat de build : différentes images ont été téléchargé ou créé comme par exemple : postgres, sonarqube ou nginx que l'on retrouve dans docker-compose.yml et docker file ou encore devops_devops-main qui est l'image résultant du docker file et correspodant à notre application principale.

Le dernier fichier créé que l'on copie comme mentionné ds le docker file qui est "app.conf" "image3"

Il s'agit de configuration nginx, permettant d'accéder à l'application python/flask, depuis le port 80 du conteneur. Il est intéressant de noter que l'on peut utiliser comme directive "server_name" le nom du conteneur tel que définit dans le docker-compose.yml, à la place de son adresse IP. Qui elle n'est pas connu à l'avance et qui change d'un build à un autre et d'une machine à une autre.

On réutilise ce même avantage dans l'application en utilisant le nom du conteneur de bdd comme "hostname" "image4"



## Some testing <a name="test"></a>
The second paragraph text

## The Licence <a name="licence"></a>
The second paragraph text

## Label <a name="label"></a>
The second paragraph text

## Who did what ? <a name="who"></a>
The second paragraph text

## Team  <a name="team"></a>
The second paragraph text

## Tasks ? <a name="task"></a>
The second paragraph text

## How to launch it <a name="nasa"></a>
On se positione dans le répertoire docker : CAS 1 : construire uniquement le projet : docker-compose build CAS 2 : pour démarrer les conteneurs (avec ou sans build préexistant) docker-compose up
The second paragraph text
```
test
```
