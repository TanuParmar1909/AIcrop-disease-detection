from fastapi import APIRouter

from backend.app.schemas.crop import SupportedCropsResponse
from backend.app.services.crop_service import get_supported_crops

router = APIRouter()


@router.get(
    "/supported-crops",
    response_model=SupportedCropsResponse
)
def supported_crops():
    crops = get_supported_crops()

    return {
        "supported_crops": crops
    }