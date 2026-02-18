# 🚀 Hybrid Database Performance Project: FastAPI + PostgreSQL + MongoDB

This project demonstrates a high-performance, asynchronous FastAPI application that integrates both **Relational (PostgreSQL)** and **NoSQL (MongoDB)** databases. It was designed to showcase hybrid data management and efficient API structuring.

## 🛠️ Tech Stack

- **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Python)
- **SQL Database:** PostgreSQL (User data management)
- **NoSQL Database:** MongoDB (Event and activity logs)
- **Server:** Uvicorn (ASGI)
- **Database Drivers:** `motor` (MongoDB) and `psycopg2` (PostgreSQL)

## 🌟 Key Features

- **Asynchronous Processing:** High-concurrency support using Python's `async/await` syntax.
- **Data Aggregation:** Seamlessly fetches and combines data from two different database engines in a single endpoint (`/all-data`).
- **Interactive Documentation:** Automated API documentation provided by Swagger UI.
- **Hybrid Architecture:** Uses PostgreSQL for structured user data and MongoDB for flexible, document-based event storage.

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have Python 3.9+, PostgreSQL, and MongoDB installed on your local machine.

### 2. Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/BozgunBer-2506/Performance_MongoDB_1802.git

cd Performance_MongoDB_1802

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

### 3. Running the Application

Start the FastAPI server:

```bash
python -m uvicorn app.main:app --port 8001 --reload
```

## 🐳 Docker Deployment

To run this project locally using Docker:

1. **Build the image:**

```bash
docker build -t fastapi-app .
```

2. **Run the container:**

```bash
docker run -p 8001:8001 \
  -e DB_PASS=your_password \
  -e DB_HOST=host.docker.internal \
  -e MONGO_URL=mongodb://host.docker.internal:27017 \
  fastapi-app
```

The app will be available at `http://localhost:8001/all-data`

## 📍 API Endpoints

- `GET /`: Welcome message and status check.
- `GET /all-data`: Combined data from PostgreSQL and MongoDB.
- `GET /docs`: Interactive Swagger UI documentation.

## 👤 Author

- **Yavuz Baris Özgün - The_Bozgun** - _Backend Developer_

---

\_Note: This project was developed as part of a database performance and integration study.
