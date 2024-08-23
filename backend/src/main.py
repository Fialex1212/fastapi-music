from fastapi import FastAPI
from .admin import init_admin
from .cors import add_cors
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
add_cors(app)
init_admin(app, engine)


@app.get("/")
def root():
    return "Hello world"

