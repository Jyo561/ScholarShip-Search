from fastapi import APIRouter, HTTPException
from models.scholarshipRequest import ScholarshipRequest  # Corrected import statement
from typing import Optional
from services.post_service import get_all_posts

router = APIRouter()

@router.post("/scholarships/")
async def get_scholarship_recommendations(request_data: ScholarshipRequest):
    try:
        caste = request_data.caste
        religion = request_data.religion
        converted = request_data.converted
        print(caste) 
        return get_all_posts(caste, religion, converted)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

