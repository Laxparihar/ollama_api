from fastapi import FastAPI
from routes import ollama_routes
import uvicorn

app = FastAPI()

# Include routes
app.include_router(ollama_routes.router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
