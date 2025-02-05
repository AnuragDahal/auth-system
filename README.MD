# FastAPI Authentication System

This project is a FastAPI-based authentication system that provides user signup, login, and profile management functionalities. It uses MongoDB as the database and JWT for authentication.

## Features

- User Signup
- User Login
- User Profile
- Password Hashing
- JWT Authentication
- Structured API Responses

## API Endpoints
 SignUp: `POST /auth/signup`
 Login: `POST /auth/login`
 Profile: `GET /user/profile`


## Requirements

- Python 3.12+
- MongoDB
- FastAPI
- Pydantic
- Motor
- JWT

## Project Structure

```sh
auth-system/
├── app/
│   ├── config/
│   │   ├── database.py
│   │   ├── dependencies.py
│   │   └── env.py
│   ├── services/
│   │   ├── authhandler.py
│   │   ├── errorhandlers.py
│   │   └── userhandler.py
│   ├── models/
│   │   └── schemas.py
│   ├── routes/
│   │   ├── auth.py
│   │   └── user.py
│   ├── utils/
│   │   ├── jwtutil.py
│   │   ├── passhashutils.py
│   │   └── response.py
│   └── main.py
├── .env
├── requirements.txt
└── README.MD
```

## Installation

1. Clone the repository:

```sh
git clone https://github.com/yourusername/auth-system.git
cd auth-system

2. Install the dependencies:

```sh
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add the following environment variables:

```sh
MONGO_URI="mongodb+srv://dahalcodecraft:WWpH6yh8Ssvs9ej7@projects.jp6z5.mongodb.net/"
SECRET_KEY = "4d2d63872da9bacbe250ddf9c2c948ff0a2664aece7a988827b8a67d88cda078"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 7
```

4. Run the FastAPI server:

```sh
uvicorn main:app --reload
```

The server will start at `http://localhost:8000`.


Happy coding! 🚀