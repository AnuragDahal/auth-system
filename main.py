from fastapi import FastAPI, Request
from app.routes import user, auth
from fastapi.middleware.cors import CORSMiddleware
from app.config.database import client
from starlette.middleware.sessions import SessionMiddleware
from app.config.env import Environment
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


env = Environment()

app = FastAPI(title="Auth", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["http://localhost:5173", "http://localhost:8000"],
    allow_methods=["*"],
    allow_headers=["*"],
)
try:
    client.admin.command("ping")
    print("Connected to MongoDB")
except Exception as e:
    print("Failed to connect to MongoDB")
    print(e)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Customize the response as needed
    return JSONResponse(
        status_code=422,
        content={
            "detail": "Invalid email type "},
    )


@app.get('/')
def root():
    return {"message": "Welcome, navigate to /docs for documentation."}


app.include_router(auth.router)
app.include_router(user.router)
