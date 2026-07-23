## Dockerfile
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## docker-compose.yml
```yaml
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/app
    depends_on:
      - db
    environment:
      - MONGO_URL=mongodb://db:27017

  db:
    image: mongo
    volumes:
      - mongo-data:/data/db

volumes:
  mongo-data:
```

## How to run this project

```bash
# Clone the repo
git clone https://github.com/yourusername/docker-notes-api.git
cd docker-notes-api

# Build and start both containers (web + db)
docker compose up -d --build

# Check both services are running
docker compose ps
```

App will be available at: `http://localhost:5000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|--------------|
| GET    | `/`      | Health check message |
| POST   | `/notes` | Add a new note |
| GET    | `/notes` | List all saved notes |

### Example requests (PowerShell)
```powershell
# Add a note
Invoke-RestMethod -Uri "http://localhost:5000/notes" -Method Post -ContentType "application/json" -Body '{"text":"my first docker note"}'

# Get all notes
Invoke-RestMethod -Uri "http://localhost:5000/notes" -Method Get
```

### Example requests (curl / Linux / Mac)
```bash
curl -X POST http://localhost:5000/notes -H "Content-Type: application/json" -d '{"text":"my first docker note"}'
curl http://localhost:5000/notes
```

## Key Docker concepts practiced

| Concept | How it was used |
|---|---|
| **Image vs Container** | Built `my-flask-app` image, ran multiple containers from it |
| **Dockerfile** | Layered build: base image → dependencies → app code |
| **Volumes** | `mongo-data:/data/db` — MongoDB data persists across container recreation |
| **Bind Mounts** | `.:/app` — live code mounted into the container during development |
| **Custom Networks** | `web` container reaches `db` container via hostname `db`, resolved by Docker's internal DNS |
| **Docker Compose** | Single command (`docker compose up -d`) starts the entire multi-container stack |

## Useful commands used during development

```bash
docker build -t my-flask-app .          # build custom image
docker run -d -p 5000:5000 --name web my-flask-app   # run container
docker ps                                # list running containers
docker logs web                          # view container logs
docker exec -it web bash                 # shell into a running container
docker volume create my-data             # create a named volume
docker network create my-network         # create a custom network
docker compose up -d --build             # build + start via Compose
docker compose down                      # stop and remove containers
docker compose ps                        # check Compose service status
```

## What I'd improve next
- Add DELETE/UPDATE endpoints for full CRUD
- Add input validation and error handling
- Add a `.env` file for configuration instead of hardcoded values
- Add automated tests