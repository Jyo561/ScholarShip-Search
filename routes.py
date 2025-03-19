from fastapi import APIRouter
from controllers import user_controller, post_controller

router = APIRouter()

# Include API controllers
router.include_router(user_controller.router, prefix="/users", tags=["Users"])
router.include_router(post_controller.router, prefix="/posts", tags=["Posts"])

