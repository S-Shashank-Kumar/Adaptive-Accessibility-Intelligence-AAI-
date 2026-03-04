"""Guided Mode Routes - Multi-step wizard for ADHD-friendly interface"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import get_db
from app.models import User
from app.schemas import TextSimplifyRequest
from app.services.guided_mode import GuidedModeService, GuidedStep
from app.dependencies import get_current_user

router = APIRouter(prefix="/guided", tags=["guided-mode"])


class GuidedStepRequest(BaseModel):
    """Request for guided mode step"""
    step: str
    data: dict = {}


class GuidedStepResponse(BaseModel):
    """Response for guided mode step"""
    step: str
    instructions: dict
    progress: dict
    can_proceed: bool
    error: str = None


@router.get("/config")
async def get_guided_config(current_user: User = Depends(get_current_user)):
    """
    Get guided mode configuration
    
    Args:
        current_user: Authenticated user
        
    Returns:
        Guided mode configuration
    """
    config = GuidedModeService.get_guided_mode_config()
    
    return {
        "config": config,
        "user_guided_mode_enabled": current_user.accessibility_profile.guided_mode if current_user.accessibility_profile else True
    }


@router.post("/next")
async def next_step(
    request: GuidedStepRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Proceed to next guided mode step
    
    Args:
        request: Current step and data
        current_user: Authenticated user
        db: Database session
        
    Returns:
        Next step instructions
    """
    try:
        current_step = GuidedStep(request.step)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid step: {request.step}"
        )
    
    # Validate current step
    is_valid, error = GuidedModeService.validate_step_completion(current_step, request.data)
    if not is_valid:
        return GuidedStepResponse(
            step=request.step,
            instructions=GuidedModeService.get_step_instructions(current_step),
            progress=GuidedModeService.get_progress(current_step),
            can_proceed=False,
            error=error
        )
    
    # Get next step
    next_step = GuidedModeService.get_next_step(current_step)
    
    if not next_step:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Already at final step"
        )
    
    return GuidedStepResponse(
        step=next_step.value,
        instructions=GuidedModeService.get_step_instructions(next_step),
        progress=GuidedModeService.get_progress(next_step),
        can_proceed=True
    )


@router.post("/previous")
async def previous_step(
    request: GuidedStepRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Go to previous guided mode step
    
    Args:
        request: Current step
        current_user: Authenticated user
        db: Database session
        
    Returns:
        Previous step instructions
    """
    try:
        current_step = GuidedStep(request.step)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid step: {request.step}"
        )
    
    # Get previous step
    prev_step = GuidedModeService.get_previous_step(current_step)
    
    if not prev_step:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Already at first step"
        )
    
    return GuidedStepResponse(
        step=prev_step.value,
        instructions=GuidedModeService.get_step_instructions(prev_step),
        progress=GuidedModeService.get_progress(prev_step),
        can_proceed=True
    )


@router.get("/instructions/{step}")
async def get_step_instructions(
    step: str,
    current_user: User = Depends(get_current_user)
):
    """
    Get instructions for a specific guided mode step
    
    Args:
        step: Step name
        current_user: Authenticated user
        
    Returns:
        Step instructions
    """
    try:
        guided_step = GuidedStep(step)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid step: {step}"
        )
    
    return {
        "step": step,
        "instructions": GuidedModeService.get_step_instructions(guided_step),
        "progress": GuidedModeService.get_progress(guided_step)
    }
