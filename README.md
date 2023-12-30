# _Note App API_

## _Where to start_

### Setup

Create .env file from .env.default then setup username and password for MongoDB

If it necessarily, change APP_API_LOCATION and APP_DB_LOCATION.

Create docker network

```yaml
docker network create notes_network
```

### Build application

```yaml
docker-compose up --build -d
```

### In case of changed source code:

Manually **DOWN** and **REBUILD** the containers:

```yaml
docker-compose down
docker-compose up --build -d
```

## In case if you just need to run application without rebuild do not use --build key

```yaml
docker-compose up -d
```

# To test this API

You can use [Postman](https://learning.postman.com/docs/introduction/overview/), for example.

Hope it has been helpful!
