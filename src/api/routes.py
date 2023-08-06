from fastapi import APIRouter, FastAPI

from src.api.v1.resources import shipping_quotation

api_router = APIRouter(prefix="/api/v1")


@api_router.get("/health_check")
async def health_check():
    return {"message": "I'm OK"}


def init_app(app: FastAPI) -> None:
    api_router.include_router(shipping_quotation.router)
    app.include_router(api_router)
