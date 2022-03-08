from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    app = FastAPI()

    # configure cors policy to global for now
    # TODO: change this later
    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # routes section here
    from app.users import router as users_router
    app.include_router(users_router, tags=["User Router"])

    @app.get("/", tags=["Root"])
    async def root():
        return {"message": "Server is up!!"}

    return app
