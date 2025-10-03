from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, db, routers

app = FastAPI(title="VisionBharatSphere API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.SQLModel.metadata.create_all(db.engine)

app.include_router(routers.auth.router, prefix="/auth")
app.include_router(routers.users.router, prefix="/users")
app.include_router(routers.products.router, prefix="/products")
app.include_router(routers.tests.router, prefix="/tests")

@app.get("/")
def root():
    return {"message":"VisionBharatSphere API is running"}
