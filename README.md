# *Note App*

## *Where to start*
To run notes app, run the commands listed below.

````
docker network create notes_network //Creates a network in which the Docker 
docker-compose up -d 
````

## In case of pulling a new code from GH repository (when a container have been already running): 
Manually **DOWN** the Docker Container by performing console command in the working directory of that container
````
docker-compose down
````
or by downing it in the interface of the Docker itself. Otherwise you won't be able to access the backend, because the container will be working with the version of the code that will have been deprecated.

Hope it have been helpful!


