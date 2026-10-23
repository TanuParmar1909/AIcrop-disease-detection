from fastapi import FastAPI
from backend.app.api.health import router as health_router
from backend.app.api.crops import router as crops_router
from backend.app.api.diseases import router as diseases_router


app = FastAPI(
    title="AI CropCare API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI CropCare API"
    }


app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["Health"]
)

app.include_router(
    crops_router,
    prefix="/api/v1",
    tags=["Crops"]
)

app.include_router(
    diseases_router,
    prefix="/api/v1",
    tags=["Diseases"]
)
