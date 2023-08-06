from fastapi import FastAPI

from src.api import routes
from src.infra.database import session
from src.infra.middlewares import cors


def create_app() -> FastAPI:
    app = FastAPI(title="Shipping Quotation Service API")

    cors.init_app(app)
    app.add_event_handler("startup", session.init_db)
    app.add_event_handler("shutdown", session.close_connection)

    routes.init_app(app)

    return app
