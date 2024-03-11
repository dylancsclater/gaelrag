from fastapi import FastAPI, HTTPException
from typing import Optional
import asyncio
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    query: str

async def call_llm_async(query: str) -> str:
    """
    Simulate an async call to your language model (LLM).
    Replace this function's body with your actual LLM call.
    """
    # Simulate a delay
    await asyncio.sleep(1)
    return f"Response to '{query}'"

@app.post("/get_response")
async def get_response(query: Query):
    """
    Endpoint to get a response from the LLM for a given query.
    Now expects a JSON body with a "query" field.
    """
    response = await call_llm_async(query.query)
    return {"query": query.query, "response": response}




