from fastapi import FastAPI
from .database import engine, Base
from .routes import router
import uvicorn

app = FastAPI(
    title="URL Shortener API",
    description="A simple URL shortener API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
