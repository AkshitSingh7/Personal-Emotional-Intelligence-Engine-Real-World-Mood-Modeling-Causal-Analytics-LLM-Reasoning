import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class MoodLLM:
    def __init__(self, model_path="models/student_qwen7b"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Loading Student Model on {self.device}...")
        
   
        self.model_name = "Qwen/Qwen2.5-7B-Instruct" 
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
      
    def generate_insight(self, context_data):
        """
        Generates the structured JSON analysis.
        """
        system_prompt = """You are an Emotional Intelligence Engine. 
        Analyze the following user data and output a JSON with: 
        summary, causal_factors, and actionable_advice."""
        
        user_prompt = f"""
        Date: {context_data.get('date')}
        Mood: {context_data.get('mood')}
        Sleep: {context_data.get('sleep')}
        Steps: {context_data.get('steps')}
        
        Provide structured psychological analysis.
        """

        return {
            "summary": "User shows signs of fatigue linked to low sleep.",
            "advice": "Prioritize recovery tonight. No screens after 10 PM."
        }
