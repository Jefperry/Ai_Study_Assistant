# Prompt Templates for HuggingFace FLAN-T5-Small
# Structured prompts for consistent AI model outputs

class PromptTemplates:
    """
    Collection of optimized prompts for google/flan-t5-small model.
    Designed for consistent and high-quality text summarization.
    """
    
    @staticmethod
    def get_summarization_prompt(text: str) -> str:
        """
        Generate summarization prompt for FLAN-T5-small.
        
        Args:
            text (str): Input text to summarize
            
        Returns:
            str: Formatted prompt for the model
        """
        return f"""Summarize the following text into 3-5 key points. Focus on the main concepts and important details:

{text}

Summary:"""

    @staticmethod
    def get_content_type_prompt(text: str, content_type: str = "general") -> str:
        """
        Generate content-type specific summarization prompt.
        
        Args:
            text (str): Input text to summarize
            content_type (str): Type of content (science, history, literature, etc.)
            
        Returns:
            str: Content-specific formatted prompt
        """
        
        content_instructions = {
            "science": "Focus on key concepts, processes, and scientific principles.",
            "history": "Highlight important events, dates, people, and cause-effect relationships.", 
            "literature": "Emphasize themes, characters, plot points, and literary devices.",
            "math": "Focus on formulas, theorems, problem-solving steps, and key concepts.",
            "general": "Focus on the main concepts and important details."
        }
        
        instruction = content_instructions.get(content_type, content_instructions["general"])
        
        return f"""Summarize the following {content_type} text into 3-5 key points. {instruction}

{text}

Summary:"""

    @staticmethod 
    def get_chunk_combination_prompt(chunks: list) -> str:
        """
        Create prompt for combining multiple summarized chunks.
        
        Args:
            chunks (list): List of summarized text chunks
            
        Returns:
            str: Prompt for combining chunks into final summary
        """
        combined_chunks = "\n\n".join([f"Section {i+1}: {chunk}" for i, chunk in enumerate(chunks)])
        
        return f"""Combine these summarized sections into one coherent summary with 3-5 main points:

{combined_chunks}

Final Summary:"""