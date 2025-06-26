## Running the Project with Docker

This project is containerized using Docker and Docker Compose for easy setup and deployment. Below are the instructions and details specific to this project:

### Project-Specific Docker Requirements
- **Python Version:** 3.11 (as specified in the Dockerfile: `python:3.11-slim`)
- **System Dependencies:**
  - `gcc` and `libpq-dev` are installed for compatibility with packages like `psycopg2` (PostgreSQL support) and `Pillow` (image processing), though the current setup uses SQLite.
- **Virtual Environment:** All Python dependencies are installed in an isolated virtual environment (`/app/.venv`).

### Environment Variables
- The Docker Compose file includes a commented-out `env_file: ./.env` line. If your project requires environment variables, create a `.env` file in the project root and uncomment this line in `docker-compose.yml`.
- No environment variables are strictly required for the default SQLite setup.

### Build and Run Instructions
1. **(Optional) Prepare your `.env` file:**
   - If your project needs environment variables, copy `.env.example` to `.env` and fill in the values, or create a `.env` file as needed.
2. **Build and start the application:**
   ```sh
   docker compose up --build
   ```
   This will build the Docker image and start the Django application in a container.

### Special Configuration Notes
- **Database:**
  - The project uses a local SQLite database (`db.sqlite3`) by default. No external database service is required.
  - If you want to persist database changes on the host machine, uncomment the `volumes` section in `docker-compose.yml`:
    ```yaml
    volumes:
      - ./db.sqlite3:/app/db.sqlite3
    ```
  - If you switch to PostgreSQL or another database, update the `docker-compose.yml` and Django settings accordingly.
- **User Permissions:**
  - The container runs as a non-root user (`appuser`) for improved security.
- **Entrypoint:**
  - The default command uses Gunicorn to serve the Django application: `gunicorn bookapi.wsgi:application --bind 0.0.0.0:8000 --workers 3`

### Exposed Ports
- **8000:** The Django application is exposed on port 8000. Access the app at [http://localhost:8000](http://localhost:8000).

---

_These instructions are specific to this project's Docker setup. For further customization, refer to the `Dockerfile` and `docker-compose.yml` in the repository._
