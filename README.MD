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

## Dummy Data
email:user@gmail.com
password:Password@123

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
│   ├── models/
│   │   └── schemas.py
│   ├── routes/
│   │   ├── auth.py
│   │   └── user.py
│   ├── services/
│   │   ├── authhandler.py
│   │   ├── errorhandlers.py
│   │   └── userhandler.py
│   └── utils/
│       ├── jwtutil.py
│       ├── passhashutils.py
│       └── response.py
├── .env
├── main.py
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
MONGO_URI="mongodb+srv://<username>:<password>@projects.jp6z5.mongodb.net/"
SECRET_KEY = "4d2d63872da9bacbe250ddf9c2c948ff0a2664aece7a988827b8a67d88cda078"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 7
```

4. Run the FastAPI server:

```sh
uvicorn main:app --reload
```

The server will start at `http://localhost:8000`.

## Testing Protected Routes

To test the protected routes, you can use Postman by following these steps:

1. **Obtain a Token**:
   - First, obtain a JWT token by logging in through the `/auth/login` endpoint. Make sure to copy the token from the response.

2. **Set Up Authorization**:
   - In Postman, create a new request for the protected route you want to test.
   - Go to the "Authorization" tab.
   - Select "Bearer Token" from the "Type" dropdown.
   - Paste the copied token into the "Token" field.

3. **Send the Request**:
   - Ensure the request method and URL are correct.
   - Send the request to test the protected route.

By following these steps, you can successfully test the protected routes using Postman with the token in the authorization headers as a Bearer Token.


Happy coding! 🚀