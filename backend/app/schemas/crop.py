from pydantic import BaseModel


class SupportedCropsResponse(BaseModel):
    supported_crops: list[str]