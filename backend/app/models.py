"""SQLAlchemy Models for AAI"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class User(Base):
    """User Model"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    full_name = Column(String(255), nullable=True)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    accessibility_profile = relationship("AccessibilityProfile", back_populates="user", uselist=False)
    simplifications = relationship("TextSimplification", back_populates="user")


class AccessibilityProfile(Base):
    """User Accessibility Preferences"""
    __tablename__ = "accessibility_profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    
    # Visual Adjustments
    font_size = Column(Integer, default=16)  # pixels
    line_spacing = Column(Float, default=1.5)  # multiplier
    letter_spacing = Column(Float, default=0.0)  # pixels
    font_family = Column(String(50), default="system")  # "system", "OpenDyslexic", "Arial", "Georgia", "Verdana", "Trebuchet"
    color_overlay = Column(String(50), default="none")  # "none", "blue", "green", "yellow", "sepia"
    high_contrast_mode = Column(Boolean, default=False)
    dark_mode = Column(Boolean, default=False)
    
    # Content Controls
    simplify_text = Column(Boolean, default=False)
    reading_level = Column(String(20), default="intermediate")  # "basic", "intermediate", "advanced"
    
    # Interaction Controls
    speech_rate = Column(Float, default=1.0)  # 0.5 to 2.0
    
    # Motion & Sensory
    reduce_motion = Column(Boolean, default=False)
    reduce_animation = Column(Boolean, default=False)
    sound_enabled = Column(Boolean, default=True)
    vibration_enabled = Column(Boolean, default=True)
    
    # Advanced
    minimal_mode = Column(Boolean, default=False)
    guided_mode = Column(Boolean, default=False)
    show_avatar = Column(Boolean, default=False)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="accessibility_profile")


class TextSimplification(Base):
    """Text Simplification Cache"""
    __tablename__ = "text_simplifications"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    original_text = Column(Text, nullable=False)
    simplified_text = Column(Text, nullable=False)
    reading_level = Column(String(20), default="intermediate")
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="simplifications")
