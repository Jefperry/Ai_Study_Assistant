# AI Client - Main orchestrator for AI services
# This file will coordinate between summarization and flashcard generation

from .summarizer_hf import HuggingFaceSummarizer
from .flashcard_generator import FlashcardGenerator

class AIClient:
    """
    Main AI service coordinator for text summarization and flashcard generation.
    Uses google/flan-t5-small for memory-optimized performance (~500MB).
    """
    
    def __init__(self):
        self.summarizer = HuggingFaceSummarizer()
        self.flashcard_generator = FlashcardGenerator()
    
    def generate_summary_and_flashcards(self, text: str, max_length: int = 10000):
        """
        Main method to process text and return summary + flashcards.
        
        Args:
            text (str): Input text to process
            max_length (int): Maximum character length (default: 10000)
            
        Returns:
            dict: {"summary": str, "flashcards": [{"q": str, "a": str}]}
        """
        # Implementation will be added in Phase C
        pass