from pydantic import BaseModel

class PredictionRequest(BaseModel):
    image_path: str

class PredictionResponse(BaseModel):
    predicted_class: int
    confidence: float
    success: bool
    message: str = None
    fruit: str = None
    disease: str = None