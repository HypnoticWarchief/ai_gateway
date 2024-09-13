from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from chat import ChatModel, validate_params
from config import DEFAULT_MODEL, DEFAULT_MAX_TOKENS, DEFAULT_TEMPERATURE, GUARDRAILS

app = FastAPI()

# Request body model
class ChatRequest(BaseModel):
    prompt: str
    model_name: str = Field(DEFAULT_MODEL, description="Optional model name. Default is the default model.")
    max_tokens: int = Field(DEFAULT_MAX_TOKENS, description="Optional max tokens. Default is 100.")
    temperature: float = Field(DEFAULT_TEMPERATURE, description="Optional temperature. Default is 0.7.")
    guardrails: str = Field(GUARDRAILS, description="Optional Guardrails. Default is False")


@app.post("/chat/")
async def chat(request: ChatRequest):
    try:
        # Validate the guardrails
        validate_params(request.max_tokens, request.temperature)

        # Create an instance of the ChatModel with parameters from the request
        chat_model = ChatModel(
            model_name=request.model_name,
            max_tokens=request.max_tokens,
            temperature=request.temperature
        )

        # Process the prompt using the appropriate AI model
        response = chat_model.process_prompt(request.prompt)
        
        return {"model_name": request.model_name, "response": response}
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Run with: uvicorn main:app --reload