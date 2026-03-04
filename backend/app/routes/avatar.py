"""Avatar Routes - Sign Language Translation"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.schemas import TextSimplifyRequest
from app.services.avatar import SignLanguageAvatarService
from app.dependencies import get_current_user

router = APIRouter(prefix="/avatar", tags=["avatar"])


@router.post("/sign")
async def generate_sign_language(
    request: TextSimplifyRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Generate sign language avatar animation for text
    
    Args:
        request: Text to convert to sign language
        current_user: Authenticated user
        db: Database session
        
    Returns:
        Avatar animation metadata and instructions
        
    Raises:
        HTTPException: If text is invalid
    """
    if not request.text.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Text cannot be empty"
        )
    
    if len(request.text) > 1000:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Text is too long (max 1000 characters)"
        )
    
    try:
        metadata = SignLanguageAvatarService.generate_avatar_metadata(request.text)
        return {
            "success": True,
            "avatar_data": metadata
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error generating sign language animation: {str(e)}"
        )


@router.get("/languages")
async def get_sign_languages(current_user: User = Depends(get_current_user)):
    """
    Get available sign language variants
    
    Args:
        current_user: Authenticated user
        
    Returns:
        Dictionary of available sign languages
    """
    return {
        "languages": SignLanguageAvatarService.get_sign_language_variants(),
        "current": "ASL"
    }


@router.post("/segment")
async def segment_for_avatar(
    request: TextSimplifyRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Split text into segments for sequential avatar animation
    
    Args:
        request: Text to segment
        current_user: Authenticated user
        db: Database session
        
    Returns:
        List of animation segments
    """
    if not request.text.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Text cannot be empty"
        )
    
    try:
        segments = SignLanguageAvatarService.split_text_for_avatar(request.text)
        return {
            "segments": segments,
            "total_segments": len(segments)
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error segmenting text: {str(e)}"
        )
