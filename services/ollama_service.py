import json
import logging
from fastapi import HTTPException
import httpx

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ollama_service")


async def get_generated_text(prompt: str, text: str, model: str):
    url = "http://localhost:11434/api/generate"
    final_prompt = f"""
    {prompt}
    <text>
    {text}
    </text>
    """
   
    async with httpx.AsyncClient(timeout=60.0) as client:
        try:
            logger.info("Sending request to %s with model: %s", url, model)
            response = await client.post(url, json={"model": model, "prompt": final_prompt, 'temperature': 0, "format": 'json'})
            response.raise_for_status()
            combined_response = ""
            for line in response.text.splitlines():
                if line.strip():
                    try:
                        data = json.loads(line)
                        if "response" in data:
                            combined_response += data["response"]
                    except json.JSONDecodeError:
                        logger.warning("Failed to decode JSON line: %s", line)
                        continue  

            #logger.info("Received response successfully")
            return {"response": combined_response}

        except httpx.RequestError as e:
            logger.error("Error communicating with the server: %s", str(e))
            raise HTTPException(status_code=500, detail=f"Error communicating with the server: {str(e)}")
        except httpx.HTTPStatusError as e:
            logger.error("HTTP Error: %s - %s", e.response.status_code, e.response.text)
            raise HTTPException(status_code=e.response.status_code, detail="Error occurred while fetching generated text.")
