# Main Imports

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mongoengine import connect

# Routes Import

from routes.prediction import router as prediction_router
from routes.user import router as user_router
from routes.user import router as user_router
from routes.auth import router as auth_router
from routes.password_reset import router as password_reset_router
from routes.item import router as item_router


# Running FastAPI app

app = FastAPI()


origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


connect(host='mongodb://localhost:27017/charaka_db')

app.include_router(prediction_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(password_reset_router)
app.include_router(item_router)

