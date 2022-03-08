from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import (
    get_swagger_ui_oauth2_redirect_html,
    get_swagger_ui_html
)
from fastapi.openapi.utils import get_openapi

from app.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title="Fastapi",
        redoc_url=None
    )

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

    # add mount to static files
    app.mount("/static", StaticFiles(directory="static"), name="static")

    # add custom openapi documentation
    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema

        openapi_schema = get_openapi(
            title='Microservice Boilerplate',
            version='1.1.0',
            routes=app.routes,
        )

        app.openapi_schema = openapi_schema
        return app.openapi_schema

    app.openapi = custom_openapi

    # routes section here
    from app.users import router as users_router
    app.include_router(users_router, tags=["User Router"])

    @app.get("/", tags=["Root"])
    async def root():
        return {"message": "Server is up!!"}

    @app.get("/swagger-ui.html", include_in_schema=False)
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(
            openapi_url=f"{settings.POST_API_HOST}/openapi.json",
            title=app.title + " - Swagger UI",
            oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
            swagger_js_url=f"{settings.POST_API_HOST}/static/swagger-ui-bundle.js",
            swagger_css_url=f"{settings.POST_API_HOST}/static/swagger-ui.css",
        )

    @app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
    async def swagger_ui_redirect():
        return get_swagger_ui_oauth2_redirect_html()

    return app
