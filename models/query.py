from pydantic import BaseModel
from typing import Optional
class Query(BaseModel):
    prompt: str
    text: str 
    model: Optional[str] = "llama3.1:8b"
  
