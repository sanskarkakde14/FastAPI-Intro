![j](https://alasco.tech/_astro/fastapi-logo.d1a6ac6e_2uVbaF.webp)

# FastAPI Blog App ⏩📝

This FastAPI project showcases a fully functional blog application with CRUD operations, password hashing using bcrypt, token authentication with OAuth2, features like APIRouter(), JWT (JSON Web Tokens), Pydantic schemas, and SQLAlchemy for ORM.

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Directory Structure](#directory-structure)


## Features

- **CRUD Operations:** Allows Create, Read, Update, and Delete operations on blog posts.
- **Hashing with Bcrypt:** Ensures secure password storage and authentication.
- **Token Authentication:** Uses OAuth2 with JWT for user authentication and authorization.
- **APIRouter():** Organizes API endpoints for modularity and readability.
- **Pydantic Schemas:** Implements Pydantic models for data validation and serialization.
- **SQLAlchemy ORM:** Utilizes SQLAlchemy for object-relational mapping and database interactions.
- **Swagger API UI:** Utilizes Swagger for interactive client.(can be accessed via localhost/docs endpoint).
  
## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/your_username/fastapi-blog.git
2. Navigate to the project directory:
   ```sh
   cd FastAPI-Intro
3. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate  # Windows
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
5. Run the FastAPI application:
   ```sh
   uvicorn blog.main:app --reload

## Directory Tree
```sh
├── blog
│   ├── __init__.py
│   ├── database.py
│   ├── hashing.py
│   ├── main.py
│   ├── models.py
│   ├── oauth2.py
│   ├── repository
│   │   ├── blog.py
│   │   └── user.py
│   ├── routers
│   │   ├── __init__.py
│   │   ├── authentication.py
│   │   ├── blog.py
│   │   └── user.py
│   ├── schemas.py
│   └── token.py
├── blog.db
└── requirements.txt
