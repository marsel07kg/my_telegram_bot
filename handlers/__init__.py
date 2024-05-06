from aiogram import Router

def setup_routers() -> Router:
    from . import (
    start,
    registration,
    profile,
    )
    router = Router()
    router.include_router(start.router)
    router.include_router(registration.router)
    router.include_router(profile.router)

    return router