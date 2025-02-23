from fastapi import FastAPI
from .routers import table

app = FastAPI()

# Routers
app.include_router(table.router)

@app.get("/")
def root():
    return {"message": "Hola Mundo desde FastAPI!"}
