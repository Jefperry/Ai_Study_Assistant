# Rule-based Flashcard Generator
# Extracts key terms and definitions using pattern matching

import re
from typing import List, Dict


class FlashcardGenerator:
    """
    Rule-based flashcard generation using pattern matching and heuristics.
    Extracts key terms and definitions from summary text.
    """

    def __init__(self):
        # Define patterns for different types of content
        self.definition_patterns = [
            r'(.+?)\s+is\s+(.+?)\.',
            r'(.+?)\s+means\s+(.+?)\.',
            r'(.+?)\s+refers to\s+(.+?)\.',
            r'(.+?)\s+is defined as\s+(.+?)\.'
        ]

        self.enumeration_patterns = [
            r'(.+?)\s+types of\s+(.+?)\s+are\s+(.+?)\.',
            r'(.+?)\s+examples include\s+(.+?)\.',
            r'(.+?)\s+such as\s+(.+?)\.'
        ]

    def generate_flashcards(self, summary_text: str, max_cards: int = 8) -> List[Dict[str, str]]:
        """
        Generate flashcards from summary text using rule-based extraction.

        Args:
            summary_text (str): Text to extract flashcards from
            max_cards (int): Maximum number of flashcards to generate

        Returns:
            List[Dict[str, str]]: List of flashcard objects with 'q' and 'a' keys
        """
        # Implementation will be added in Phase C
        flashcards = []

        # Extract definition-based flashcards
        flashcards.extend(self._extract_definitions(summary_text))

        # Extract enumeration-based flashcards
        flashcards.extend(self._extract_enumerations(summary_text))

        # Extract key terms
        flashcards.extend(self._extract_key_terms(summary_text))

        # Return up to max_cards unique flashcards
        return flashcards[:max_cards]

    def _extract_definitions(self, text: str) -> List[Dict[str, str]]:
        """Extract definition-based flashcards."""
        # Implementation will be added in Phase C
        return []

    def _extract_enumerations(self, text: str) -> List[Dict[str, str]]:
        """Extract enumeration-based flashcards."""
        # Implementation will be added in Phase C
        return []

    def _extract_key_terms(self, text: str) -> List[Dict[str, str]]:
        """Extract key terminology flashcards."""
        # Implementation will be added in Phase C
        return []
