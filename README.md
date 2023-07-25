# CampusCompass CRUD API

This is a simple CRUD API written in Python FastAPI to interact with a Postgres database.

It simply describes the features that a campus, building, and features of those buildings may have.

For the time being, we are leaving it at the __R__ in CRUD 😂.

### Setting up this project
Prerequisite: [Docker](docker.com)
This project consists of two components: an API and a Postgres database.
Docker-compose takes care of setup for you.
1. In your terminal, run `git clone https://github.com/aid-kov/campus-compass-api.git`
2. Run `cd campus-compass-api`
3. Finally `docker-compose up -d`

This should load the API and Postgres into Docker, available for use!
