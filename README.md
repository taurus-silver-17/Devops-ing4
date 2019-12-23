![alt text](https://img.shields.io/github/license/taurus-silver-17/Devops-ing4)
![alt text](https://img.shields.io/badge/Python-3.6-green "Logo Title Text 1")
![alt text](https://img.shields.io/badge/Docker%20Build-Passing-green)
![alt text](https://img.shields.io/badge/Docker%20Build%20-Automated-blue)
![alt text](https://img.shields.io/badge/Build-failure-red)
![alt text](https://img.shields.io/github/forks/taurus-silver-17/Devops-ing4)
![alt text](https://img.shields.io/github/repo-size/Taurus-silver-17/Devops-ing4)

# DevOps project during the 4th engineering 
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
![alt text](https://github.com/taurus-silver-17/Devops-ing4/blob/master/static/img/devops1.png)

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
  There are currently 3 containers turning: :
- "devops-db" which is a "postgre" container. 
- "devops-ci," which is the "sonarqube" container.
- The devops-main container which contains the python application and is a base for the nginx container which are deployed via docker-composes when you connect to "http://163.172.64.25:8080/truhome/".
  
![alt text](https://github.com/taurus-silver-17/Devops-ing4/blob/master/static/img/schema_docker.png)

  Here we have 4 files: 

- docker-compose.yml : here we declare our 3 services: 
1. devops-db which will be the first container for the db, we give it a name for the DNS : devops-db. 

Then we give environment variables for the creation of the postgres database.

2. devops-ci which is the 2nd container, for the CI server 
- devops-main: here we don't specify an image, since we will start from a docker file as we will create our image from our files. 

We find our environment variables since they are parameters that will be used in our configuration files. 


![alt text](https://github.com/taurus-silver-17/Devops-ing4/blob/master/static/img/imag1.png)

So we can see above, the environment variables defined at the creation of the container that we retrieve in the application.

Then we define the port parameter which allows the redirection from port 80 for our container to port 8080 of the host machine. We declare dependencies, which will allow us to say that if the specified Containers are not correctly started, we stop the build of the Container in question. 

We have a build parameter that allows us to indicate the path to the docker file. Now let's talk about the docker file: it allows us to create the image of the devops-main container. We start from a NGINX container, we copy the files we'll need later (configuration file and entry-point file). 
We then execute a series of commands to prepare and install our software dependencies. Then we will paste the Github project to the root of the web server. 

Finally, we execute the entry point via the single directive "CMD" which refers us to the "entry point". The entry point is the entry point of the container, i.e.: one or more commands to execute, once the container is created based on the constructed image, depending on the docker file. 

Once we have all this we execute: "docker-compose build" in order to build the architecture and the images according to the description provided in the file: docker-compose.yml

Finally, to instantiate the containers, we run "docker-compose-up -d". The containers will be detached in the background: 

![alt text](https://github.com/taurus-silver-17/Devops-ing4/blob/master/static/img/img2.jpeg)

Here we can see the result of build: different images have been downloaded or created as for example: postgres, sonarqube or nginx which can be found in docker-compose.yml and docker file or devops_devops-main which is the image resulting from the docker file and corresponding to our main application.

The last created file that we copy as mentioned in the docker file which is "app.conf". 

![alt text](https://github.com/taurus-silver-17/Devops-ing4/blob/master/static/img/app_conf.png)

This is nginx configuration, allowing access to the python/flask application from port 80 of the container. It is interesting to note that you can use as a "server_name" directive the name of the container as defined in the docker-compose.yml, instead of its IP address. Which it is not known in advance and which changes from one build to another and from one machine to another.

We reuse this same advantage in the application by using the name of the bdd container as "hostname". 

![alt text](https://github.com/taurus-silver-17/Devops-ing4/blob/master/static/img/ig.png)


## Some testing <a name="test"></a>
UNDER CONSTRUCTION

## The Licence <a name="licence"></a>
Licensed GNU General Public License v3.0. [View license](https://github.com/taurus-silver-17/Devops-ing4/blob/master/LICENSE)

## Label <a name="label"></a>
To create the badges like these : 
![alt text](https://github.com/taurus-silver-17/Devops-ing4/blob/master/static/img/Badges.png)

We used [shield.io](https://shields.io/)

## Who did what ? <a name="who"></a>
In this section you will find the consitution of our Team and the tasks
## Team  <a name="team"></a>
We are a team of two :
- [Lilian Delaplace (Techorem)](https://github.com/techorem)
- [Arnaud Jullemier (Taurus-silver-17)](https://github.com/taurus-silver-17)


## Tasks ? <a name="task"></a>
Here you will found our organization for this project 

![alt text](https://github.com/taurus-silver-17/Devops-ing4/blob/master/static/img/task10.png)


## How to launch it <a name="nasa"></a>
We position ourselves in the docker directory : 
- CASE 1: build only the project: 
```
docker-compose build
```
- CASE 2: to start the containers (with or without pre-existing build) 
```
docker-compose up -d
```
Then you go on "http://163.172.64.25:8080/truhome/"

## Issues <a name="issues"></a>
[Issue1](https://github.com/taurus-silver-17/Devops-ing4/issues/1)

