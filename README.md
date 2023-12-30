# notes

Simple note taking fullstack app. 

Project without deployment, but you can run it locally simple with [Docker](https://frontgr.github.io/docs/docker/docker/) with one command. 
![image](https://github.com/frontgr/notes/assets/52705623/555b6519-5cde-4a1d-8f71-1caa88d58710)

---

### Technologies Used

1. Vue
2. Docker
3. MongoDB
4. Flask

---

## How to run the app? 

Create `.env` file from `.env.default` then setup username and password for MongoDB. If it necessarily, change `APP_API_LOCATION` and `APP_DB_LOCATION`.

Create docker network:

```yaml
docker network create notes_network
```

Then, build the application: 

```yaml
docker-compose up --build -d
```

---

### Formatting rules

We use Prettier for formatting our text. See more about our configuration [here](https://frontgr.github.io/docs/prettierrc/prettierrc/).

---

Project has [MIT License](https://github.com/frontgr/notes/blob/main/LICENSE).
