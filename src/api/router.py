from fastapi import APIRouter  
  
from src.api.routes.bands import router as bands_router  

router = APIRouter()  
  
  
router.include_router(bands_router, prefix="/bands")