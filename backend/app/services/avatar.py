"""Sign Language Avatar Service"""
import logging
from typing import Optional, List

logger = logging.getLogger(__name__)

# Pre-defined ASL dictionary with common words
ASL_DICTIONARY = {
    "hello": "asl_hello.mp4",
    "goodbye": "asl_goodbye.mp4",
    "thank": "asl_thank.mp4",
    "please": "asl_please.mp4",
    "yes": "asl_yes.mp4",
    "no": "asl_no.mp4",
    "help": "asl_help.mp4",
    "person": "asl_person.mp4",
    "water": "asl_water.mp4",
    "love": "asl_love.mp4",
    "family": "asl_family.mp4",
    "friend": "asl_friend.mp4",
    "work": "asl_work.mp4",
    "time": "asl_time.mp4",
    "good": "asl_good.mp4",
    "bad": "asl_bad.mp4",
    "happy": "asl_happy.mp4",
    "sad": "asl_sad.mp4",
    "understand": "asl_understand.mp4",
    "know": "asl_know.mp4",
}


class SignLanguageAvatarService:
    """
    Service for generating sign language avatar animations
    Converts text to sign language animations for deaf/hard of hearing users
    """

    @staticmethod
    def text_to_sign_animation(text: str) -> dict:
        """
        Convert text to sign language animation instructions
        
        Args:
            text: Text to convert to sign language
            
        Returns:
            Dict with animation data and metadata
        """
        words = text.lower().split()
        animations = []
        unrecognized = []
        
        for word in words:
            # Clean word of punctuation
            clean_word = word.strip(".,!?;:")
            
            # Look up in ASL dictionary
            if clean_word in ASL_DICTIONARY:
                animations.append({
                    "word": clean_word,
                    "video": ASL_DICTIONARY[clean_word],
                    "duration": 1500,  # ms
                    "recognized": True
                })
            else:
                # Attempt to spell out word (fingerspelling)
                animations.append({
                    "word": clean_word,
                    "letters": list(clean_word.upper()),
                    "type": "fingerspell",
                    "duration": len(clean_word) * 200,  # 200ms per letter
                    "recognized": False
                })
                unrecognized.append(clean_word)
        
        return {
            "text": text,
            "animations": animations,
            "total_duration_ms": sum(a.get("duration", 0) for a in animations),
            "unrecognized_words": unrecognized,
            "avatar_style": "3d",  # Could be "2d", "3d", "video"
        }

    @staticmethod
    def get_sign_language_variants() -> dict:
        """
        Get available sign language variants
        
        Returns:
            Dict of available sign language options
        """
        return {
            "ASL": "American Sign Language",
            "BSL": "British Sign Language",
            "DSL": "Danish Sign Language",
            "FSL": "French Sign Language",
            "DGS": "German Sign Language",
            "LSF": "French Sign Language",
            "JSL": "Japanese Sign Language",
            "CSL": "Chinese Sign Language",
        }

    @staticmethod
    def split_text_for_avatar(text: str, words_per_segment: int = 5) -> List[dict]:
        """
        Split text into segments for avatar animation
        
        Args:
            text: Text to split
            words_per_segment: Number of words per animation segment
            
        Returns:
            List of animation segments
        """
        words = text.split()
        segments = []
        
        for i in range(0, len(words), words_per_segment):
            segment_words = words[i:i + words_per_segment]
            segment_text = " ".join(segment_words)
            
            animation = SignLanguageAvatarService.text_to_sign_animation(segment_text)
            animation["segment_index"] = len(segments)
            segments.append(animation)
        
        return segments

    @staticmethod
    def generate_avatar_metadata(text: str) -> dict:
        """
        Generate metadata for avatar rendering
        
        Args:
            text: Text for avatar to sign
            
        Returns:
            Metadata for frontend avatar component
        """
        animation_data = SignLanguageAvatarService.text_to_sign_animation(text)
        
        return {
            "text": text,
            "word_count": len(text.split()),
            "recognized_words": sum(1 for a in animation_data["animations"] if a["recognized"]),
            "unrecognized_words": animation_data["unrecognized_words"],
            "total_duration_seconds": animation_data["total_duration_ms"] / 1000,
            "animation_data": animation_data,
            "avatar_speed": "normal",  # Could be "slow", "normal", "fast"
        }
