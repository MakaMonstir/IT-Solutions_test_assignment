# IT Solutions test assignment

Test task for IT-Solutions company

This is a FastAPI application that interfaces with a PostgreSQL database. The application is containerized using Docker and Docker Compose for easy setup and deployment.

## Features

- FastAPI for building APIs
- PostgreSQL for the database
- Docker and Docker Compose for containerization
- Health checks for services
- Data scraping and database initialization

## Setup and Running

### Prerequisites

- Docker
- Docker Compose

### Environment Variables

Create a `.env` file in the root directory of your project with the following content:

```sh
DATABASE_URL=postgresql://postgres:postgres@db:5432/mydatabase
```

### Build and Run

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/IT-Solutions_test_assignment.git
   cd IT-Solutions_test_assignment
   ```

2. **Build and start the services:**

```sh
docker-compose build
docker-compose up
```

### Alternate way (Run locally):

1. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. **Install the required dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Run the FastAPI application locally:**

   ```sh
   uvicorn app.main:app --reload
   ```

(Optional) 4. If your want to populate your db with example data use app/dummy_data.py script. It will parse data from source.html file and paste it to DB on URL specified in .env file.

    ```sh
    python3 app/dummy_data.py
    ```

## API Endpoints

### Get 10 first ads:

    URL: /ad/
    •	Method: GET
    •	Response: list of JSONs

### Get ad by id:

URL: /ad/{ad_id}
• Method: GET
• Response: JSON
