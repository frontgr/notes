# *Note App API*

## *Where to start*
To run notes app, install the Docker, then you will need to create a Docker Network (only once) for containers to communicate, and build the containers itself:

````
docker network create notes_network
docker-compose up --build -d
````

## In case of changed source code: 
Manually **DOWN** and **BUILD** the containers:
````
docker-compose down
docker-compose up --build -d
````

## In case if you just need to down the containers and then up (without rebuilding) them again
````
docker-compose down
docker-compose up -d
````

# To test this API
You can use [Postman](https://learning.postman.com/docs/introduction/overview/), for example.

Hope it has been helpful!


