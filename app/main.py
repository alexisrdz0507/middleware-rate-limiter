from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="Middleware de Rate Limiting",
    description="Protección de APIs contra ataques",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {
        "message": "Middleware funcionando correctamente",
        "status": "OK"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)