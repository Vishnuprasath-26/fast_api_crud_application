# FastAPI CRUD Application with JWT Authentication

## Project Overview

This project is a REST API built using FastAPI, SQLAlchemy, PostgreSQL, and JWT authentication. Users can register, log in, and manage their own tasks securely.

## Technologies Used

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic
* JWT Authentication
* Passlib for password hashing
* Uvicorn

## Features

* User registration with password hashing
* User login with JWT access token
* Token expiration
* Protected routes using OAuth2
* Get current authenticated user
* Create, read, update, and delete tasks
* Task ownership: users can access only their own tasks
* Pagination for task listing
* Request validation with Pydantic

## Project Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd fastapi_crud_auth
```

### 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and configure:

* `DATABASE_URL`
* `SECRET_KEY`
* `ALGORITHM`
* `ACCESS_TOKEN_EXPIRE_MINUTES`

Use `.env.example` as a template. Do not commit your actual `.env` file or database credentials.

### 5. Run the application

```bash
python -m uvicorn main:app --reload
```

## API Documentation

After starting the application, open:

`http://127.0.0.1:8000/docs`

Use Swagger UI to test registration, login, authentication, and task CRUD endpoints.

## Authentication

Register a user, log in to receive an access token, and use the **Authorize** option in Swagger UI to test protected endpoints.

## Database

The application uses SQLAlchemy models and PostgreSQL. Database tables are created when the application starts.

## Security

Passwords are hashed before storage. Protected task endpoints require a valid JWT access token, and users can manage only their own tasks.
