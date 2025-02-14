import logging
from fastapi import APIRouter, HTTPException, Body
from fastapi.responses import StreamingResponse, JSONResponse
import httpx
from models.query import Query
from services.ollama_service import  get_generated_text

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/generate")
async def generate_text(query: Query):
    if query:
        logger.info("Received request to generate text with query")
        try:
            response = await get_generated_text(query.prompt, query.text,query.model)
           # logger.info("Successfully generated model response: %s", response)
            return JSONResponse(response)
        except Exception as e:
            logger.error("Error generating model response: %s", str(e))
            raise HTTPException(status_code=500, detail=f"Error generating model response: {str(e)}")
        


@router.post("/models/download")
async def download_model(llm_name: str = Body(..., embed=True)):
    logger.info("Received request to download model: %s", llm_name)
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:11434/api/pull",
                json={"name": llm_name}
            )
            response.raise_for_status()
            logger.info("Model %s downloaded successfully", llm_name)
            return {"message": f"Model {llm_name} downloaded successfully"}
    except httpx.RequestError as e:
        logger.error("Error downloading model %s: %s", llm_name, str(e))
        raise HTTPException(status_code=500, detail=f"Error downloading model: {str(e)}")
    
    

@router.get("/models")
async def list_models():
    logger.info("Received request to list models")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("http://localhost:11434/api/tags")
            response.raise_for_status()
            models = response.json()["models"]
            logger.info("Fetched models: %s", models)
            return {"models": models}
    except httpx.RequestError as e:
        logger.error("Error fetching models: %s", str(e))
        raise HTTPException(status_code=500, detail=f"Error fetching models: {str(e)}")
