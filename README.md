# docker-notes-api
Flask + MongoDB notes API containerized with Docker
# Docker Notes API — Flask + MongoDB

A small REST API built with Flask and MongoDB, fully containerized using Docker.
This project was built to practice core Docker concepts hands-on: images, containers,
Dockerfiles, volumes, custom networks, and Docker Compose.

## What this project demonstrates

- Writing a custom **Dockerfile** to build an application image
- Running a **MongoDB** container using the official image
- Connecting two containers via a **custom Docker network** (service discovery by hostname)
- Persisting database data using a **Docker Volume** (survives container restarts/removal)
- Orchestrating the full multi-container app using **Docker Compose**
- Testing real REST API read/write operations end-to-end

## Tech Stack
- Python (Flask) — REST API
- MongoDB — database
- PyMongo — MongoDB driver for Python
- Docker & Docker Compose

## Project Structure
docker-demo/
├── app.py # Flask app with /notes endpoints
├── requirements.txt # Python dependencies (flask, pymongo)
├── Dockerfile # Builds the Flask app image
├── docker-compose.yml # Defines web + db services
└── README.md
