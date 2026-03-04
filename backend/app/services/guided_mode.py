"""Guided Mode Service - Multi-step wizard for ADHD-friendly interface"""
import logging
from typing import Optional, List
from enum import Enum

logger = logging.getLogger(__name__)


class GuidedStep(Enum):
    """Steps in the guided mode wizard"""
    WELCOME = "welcome"
    PASTE_TEXT = "paste_text"
    SELECT_OPTIONS = "select_options"
    SIMPLIFY = "simplify"
    REVIEW = "review"
    COMPLETE = "complete"


class GuidedModeService:
    """
    Service for guided mode navigation
    Helps ADHD and cognitively overloaded users by:
    - Breaking down the interface into manageable steps
    - Auto-advancing through steps
    - Providing clear instructions at each stage
    - Limiting visible options to reduce cognitive load
    """

    STEP_SEQUENCE = [
        GuidedStep.WELCOME,
        GuidedStep.PASTE_TEXT,
        GuidedStep.SELECT_OPTIONS,
        GuidedStep.SIMPLIFY,
        GuidedStep.REVIEW,
        GuidedStep.COMPLETE,
    ]

    @staticmethod
    def get_step_instructions(step: GuidedStep) -> dict:
        """
        Get instructions for a specific guided mode step
        
        Args:
            step: Current guided mode step
            
        Returns:
            Step instructions and metadata
        """
        instructions = {
            GuidedStep.WELCOME: {
                "title": "Welcome to Guided Mode",
                "description": "This step-by-step mode will help you simplify text easily.",
                "instruction": "Click 'Next' to continue.",
                "button_label": "Start",
                "button_action": "next",
                "can_skip": False,
            },
            GuidedStep.PASTE_TEXT: {
                "title": "Paste Your Text",
                "description": "Copy and paste the text you want to simplify.",
                "instruction": "Enter your text in the text area below.",
                "button_label": "Next",
                "button_action": "next",
                "enable_components": ["text_input"],
                "disable_components": ["accessibility_panel"],
                "can_skip": False,
                "validation": "text_not_empty",
            },
            GuidedStep.SELECT_OPTIONS: {
                "title": "Choose Your Settings",
                "description": "Select how you want your text simplified.",
                "instruction": "Pick your reading level and preference.",
                "button_label": "Next",
                "button_action": "next",
                "enable_components": ["reading_level_selector", "color_overlay"],
                "disable_components": ["font_size", "line_spacing", "advanced_options"],
                "can_skip": True,
                "skip_button": "Use Defaults",
            },
            GuidedStep.SIMPLIFY: {
                "title": "Simplifying Your Text",
                "description": "Our AI is simplifying your text...",
                "instruction": "This usually takes a few seconds. Please wait.",
                "button_label": "Processing...",
                "button_action": "processing",
                "button_disabled": True,
                "show_progress": True,
                "can_skip": False,
            },
            GuidedStep.REVIEW: {
                "title": "Review Your Result",
                "description": "Here's your simplified text.",
                "instruction": "Read through it. You can copy it or go back to edit.",
                "button_label": "Done",
                "button_action": "complete",
                "enable_components": ["simplified_text_output", "copy_button", "back_button"],
                "can_skip": False,
                "can_go_back": True,
            },
            GuidedStep.COMPLETE: {
                "title": "All Done!",
                "description": "Your text has been simplified.",
                "instruction": "Great job! Would you like to simplify another text?",
                "button_label": "Start Over",
                "button_action": "reset",
                "can_skip": False,
            },
        }
        
        return instructions.get(step, {})

    @staticmethod
    def get_next_step(current_step: GuidedStep) -> Optional[GuidedStep]:
        """
        Get the next step in the sequence
        
        Args:
            current_step: Current step
            
        Returns:
            Next step, or None if at the end
        """
        try:
            current_index = GuidedModeService.STEP_SEQUENCE.index(current_step)
            if current_index < len(GuidedModeService.STEP_SEQUENCE) - 1:
                return GuidedModeService.STEP_SEQUENCE[current_index + 1]
        except ValueError:
            pass
        
        return None

    @staticmethod
    def get_previous_step(current_step: GuidedStep) -> Optional[GuidedStep]:
        """
        Get the previous step in the sequence
        
        Args:
            current_step: Current step
            
        Returns:
            Previous step, or None if at the beginning
        """
        try:
            current_index = GuidedModeService.STEP_SEQUENCE.index(current_step)
            if current_index > 0:
                return GuidedModeService.STEP_SEQUENCE[current_index - 1]
        except ValueError:
            pass
        
        return None

    @staticmethod
    def get_progress(current_step: GuidedStep) -> dict:
        """
        Get progress information for current step
        
        Args:
            current_step: Current step
            
        Returns:
            Progress metadata
        """
        try:
            current_index = GuidedModeService.STEP_SEQUENCE.index(current_step)
            total_steps = len(GuidedModeService.STEP_SEQUENCE)
            
            return {
                "current_step": current_index + 1,
                "total_steps": total_steps,
                "percentage": ((current_index + 1) / total_steps) * 100,
                "step_name": current_step.value,
            }
        except ValueError:
            return {}

    @staticmethod
    def validate_step_completion(step: GuidedStep, data: dict) -> tuple[bool, Optional[str]]:
        """
        Validate if a step has been completed
        
        Args:
            step: Current step
            data: Data from the step
            
        Returns:
            (is_valid, error_message)
        """
        if step == GuidedStep.PASTE_TEXT:
            if not data.get("text") or not data["text"].strip():
                return False, "Please paste some text to continue."
            if len(data["text"].strip()) < 10:
                return False, "Text is too short. Please paste at least 10 characters."
        
        elif step == GuidedStep.SELECT_OPTIONS:
            if not data.get("reading_level"):
                return False, "Please select a reading level."
        
        elif step == GuidedStep.SIMPLIFY:
            if not data.get("simplified_text"):
                return False, "Text simplification failed. Please try again."
        
        return True, None

    @staticmethod
    def get_guided_mode_config() -> dict:
        """
        Get complete guided mode configuration
        
        Returns:
            Complete guided mode settings
        """
        return {
            "enabled": True,
            "autoAdvance": True,
            "steps": [step.value for step in GuidedModeService.STEP_SEQUENCE],
            "total_steps": len(GuidedModeService.STEP_SEQUENCE),
            "animations_enabled": True,
            "feedback": "positive",  # "none", "subtle", "positive"
            "reduced_options": True,  # Hide advanced options
            "help_available": True,
            "can_exit_anytime": True,
        }
