from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import api.endpoints as endpoints

class Api():
    def __init__(self) -> None:
        self.client = FastAPI(
            title="API",
            description="",
            version="1.0.0",
            docs_url="/api"
        )

        self.client.add_middleware(
            CORSMiddleware,
            allow_origins=["http://localhost:4200"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        self.client.include_router(endpoints.gopro.router)

    def run(self):
        uvicorn.run(self.client, host="0.0.0.0", port=8000)