"""Text Simplification Routes"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User, TextSimplification
from app.schemas import TextSimplifyRequest, TextSimplifyResponse
from app.services.text_adapter import simplify_text as npl_simplify_text
from app.dependencies import get_current_user

router = APIRouter(prefix="/text", tags=["text"])


@router.post("/simplify", response_model=TextSimplifyResponse)
async def simplify_text(
    request: TextSimplifyRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Simplify complex text using NLP
    
    Args:
        request: TextSimplifyRequest with text and reading level
        current_user: Authenticated user
        db: Database session
        
    Returns:
        TextSimplifyResponse with simplified text
        
    Raises:
        HTTPException: If text is too short or long
    """
    # Validate text length
    if len(request.text) < 10:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Text must be at least 10 characters"
        )
    
    if len(request.text) > 5000:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Text must be less than 5000 characters"
        )
    
    # Call NLP service to simplify
    try:
        simplified = npl_simplify_text(request.text, request.reading_level)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error simplifying text: {str(e)}"
        )
    
    # Save to database for caching
    cache_entry = TextSimplification(
        user_id=current_user.id,
        original_text=request.text,
        simplified_text=simplified,
        reading_level=request.reading_level
    )
    db.add(cache_entry)
    db.commit()
    
    return {
        "original_text": request.text,
        "simplified_text": simplified,
        "reading_level": request.reading_level
    }
