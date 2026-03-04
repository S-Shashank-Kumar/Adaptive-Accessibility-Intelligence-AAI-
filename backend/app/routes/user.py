"""User Profile Routes"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User, AccessibilityProfile
from app.schemas import AccessibilityProfileResponse, AccessibilityProfileUpdate
from app.dependencies import get_current_user

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/profile", response_model=AccessibilityProfileResponse)
async def get_profile(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Get user accessibility profile
    
    Args:
        current_user: Authenticated user
        db: Database session
        
    Returns:
        AccessibilityProfileResponse
    """
    profile = db.query(AccessibilityProfile).filter(
        AccessibilityProfile.user_id == current_user.id
    ).first()
    
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
    
    return profile


@router.put("/profile", response_model=AccessibilityProfileResponse)
async def update_profile(
    profile_update: AccessibilityProfileUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Update user accessibility profile
    
    Args:
        profile_update: Updated profile data
        current_user: Authenticated user
        db: Database session
        
    Returns:
        Updated AccessibilityProfileResponse
    """
    profile = db.query(AccessibilityProfile).filter(
        AccessibilityProfile.user_id == current_user.id
    ).first()
    
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
    
    # Update only provided fields
    update_data = profile_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(profile, field, value)
    
    db.commit()
    db.refresh(profile)
    
    return profile
