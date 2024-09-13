from config import DEFAULT_MODEL, DEFAULT_MAX_TOKENS, DEFAULT_TEMPERATURE

class ChatModel:
    def __init__(self, model_name: str = DEFAULT_MODEL, max_tokens: int = DEFAULT_MAX_TOKENS, temperature: float = DEFAULT_TEMPERATURE):
        self.model_name = model_name
        self.max_tokens = max_tokens
        self.temperature = temperature

    def process_prompt(self, prompt: str) -> str:
        # Simulating different AI models
        if self.model_name == "gpt-3.5":
            return self.model_gpt_3_5(prompt)
        elif self.model_name == "gpt-4":
            return self.model_gpt_4(prompt)
        else:
            return self.default_model(prompt)

    def model_gpt_3_5(self, prompt: str) -> str:
        return f"GPT-3.5 Response: {prompt} with max tokens: {self.max_tokens}, temp: {self.temperature}"

    def model_gpt_4(self, prompt: str) -> str:
        return f"GPT-4 Response: {prompt} with max tokens: {self.max_tokens}, temp: {self.temperature}"

    def default_model(self, prompt: str) -> str:
        return f"Default Model Response: {prompt} with max tokens: {self.max_tokens}, temp: {self.temperature}"
    