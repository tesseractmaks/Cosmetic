from fastapi import APIRouter
from .api_v1.endpoints.user import router as user_router
from .api_v1.endpoints.profile import router as profile_router
from .api_v1.endpoints.product import router as product_router
from .api_v1.endpoints.brand import router as brand_router
from .api_v1.endpoints.category import router as category_router
# from .api_v1.endpoints.token import router as token_router


router = APIRouter()
router_token = APIRouter()
router.include_router(router=user_router, prefix="/users")
router.include_router(router=profile_router, prefix="/profiles")
router.include_router(router=product_router, prefix="/products")
router.include_router(router=brand_router, prefix="/brands")
router.include_router(router=category_router, prefix="/categories")

# router_token.include_router(router=token_router)
# router_token.include_router(router=token_router, prefix="/token")