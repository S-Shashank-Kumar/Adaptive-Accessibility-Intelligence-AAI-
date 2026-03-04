"""Pydantic Request/Response Schemas"""
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional


# User Schemas
class UserCreate(BaseModel):
    """User registration schema"""
    email: EmailStr
    password: str = Field(..., min_length=8)
    full_name: Optional[str] = None


class UserLogin(BaseModel):
    """User login schema"""
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    """User response schema"""
    id: int
    email: str
    full_name: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


# Accessibility Profile Schemas
class AccessibilityProfileCreate(BaseModel):
    """Accessibility profile creation"""
    font_size: int = Field(default=16, ge=12, le=32)
    line_spacing: float = Field(default=1.5, ge=1.0, le=3.0)
    letter_spacing: float = Field(default=0.0, ge=0.0, le=2.0)
    font_family: str = "system"
    color_overlay: str = "none"
    high_contrast_mode: bool = False
    dark_mode: bool = False
    simplify_text: bool = False
    reading_level: str = "intermediate"
    speech_rate: float = Field(default=1.0, ge=0.5, le=2.0)
    reduce_motion: bool = False
    reduce_animation: bool = False
    sound_enabled: bool = True
    vibration_enabled: bool = True
    minimal_mode: bool = False
    guided_mode: bool = False
    show_avatar: bool = False


class AccessibilityProfileUpdate(BaseModel):
    """Accessibility profile update (all fields optional)"""
    font_size: Optional[int] = Field(None, ge=12, le=32)
    line_spacing: Optional[float] = Field(None, ge=1.0, le=3.0)
    letter_spacing: Optional[float] = Field(None, ge=0.0, le=2.0)
    font_family: Optional[str] = None
    color_overlay: Optional[str] = None
    high_contrast_mode: Optional[bool] = None
    dark_mode: Optional[bool] = None
    simplify_text: Optional[bool] = None
    reading_level: Optional[str] = None
    speech_rate: Optional[float] = Field(None, ge=0.5, le=2.0)
    reduce_motion: Optional[bool] = None
    reduce_animation: Optional[bool] = None
    sound_enabled: Optional[bool] = None
    vibration_enabled: Optional[bool] = None
    minimal_mode: Optional[bool] = None
    guided_mode: Optional[bool] = None
    show_avatar: Optional[bool] = None


class AccessibilityProfileResponse(BaseModel):
    """Accessibility profile response"""
    id: int
    user_id: int
    font_size: int
    line_spacing: float
    letter_spacing: float
    font_family: str
    color_overlay: str
    high_contrast_mode: bool
    dark_mode: bool
    simplify_text: bool
    reading_level: str
    speech_rate: float
    reduce_motion: bool
    reduce_animation: bool
    sound_enabled: bool
    vibration_enabled: bool
    minimal_mode: bool
    guided_mode: bool
    show_avatar: bool
    updated_at: datetime

    class Config:
        from_attributes = True


# Authentication Schemas
class TokenResponse(BaseModel):
    """Token response"""
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """Token data payload"""
    email: Optional[str] = None


# Text Simplification Schemas
class TextSimplifyRequest(BaseModel):
    """Text simplification request"""
    text: str = Field(..., min_length=10, max_length=5000)
    reading_level: str = Field(default="intermediate")


class TextSimplifyResponse(BaseModel):
    """Text simplification response"""
    original_text: str
    simplified_text: str
    reading_level: str


# Health Check
class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    message: str = "AAI Backend is running"
