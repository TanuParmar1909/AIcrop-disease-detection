from fastapi import APIRouter

router = APIRouter()


@router.get("/supported-diseases")
def get_supported_diseases():
    return {
        "supported_diseases": [
            "Tomato_Early_Blight",
            "Tomato_Late_Blight",
            "Potato_Early_Blight",
            "Potato_Late_Blight",
            "Rice_Blast",
            "Wheat_Rust",
            "Maize_Common_Rust",
            "Soybean_Rust",
            "Cotton_Bacterial_Blight",
            "Chilli_Leaf_Curl"
        ]
    }