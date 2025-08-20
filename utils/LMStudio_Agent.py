
import httpx
import asyncio

LMSTUDIO_API_URL = "http://lmstudio-url/v1/chat/completions"

async def extract_LMStudio(prompt: str, text: str, model: str = "openai/gpt-oss-20b"):
    headers = {
        "Content-Type": "application/json",
        # If your gateway requires a key, uncomment the next line:
        # "Authorization": f"Bearer {os.environ['LMSTUDIO_API_KEY']}",
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": text},
        ],
        "temperature": 0.0,
        "stream": False,  # set True if your server supports streaming
    }
    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.post(LMSTUDIO_API_URL, headers=headers, json=payload)
        r.raise_for_status()
        data = r.json()
        # Defensive parsing for OpenAI-compatible servers
        msg = (data.get("choices") or [{}])[0].get("message", {})
        return msg.get("content", "")

# quick test
# asyncio.run(extract_LMStudio("You are concise.", "Say hi in one word."))



## from agents import Agent, Runner
#
#from datetime import datetime, timedelta
#import json
#import ast
#
#import httpx
#import asyncio
#
#
##def get_availability_parser_agent(prompt: str, use_model: str):
##    return Agent(
##        name="Availability Parser Agent",
##        instructions=prompt,
##        model=use_model,
##    )
##
##async def extract_OpenAI(prompt: str, text: str, model: str) -> str:
##    runner = Runner()
##    agent = get_availability_parser_agent(prompt, model)
##    result = await runner.run(agent, text)
##
##    return result.final_output
#
#LMSTUDIO_API_URL = "https://pineapple.fff.ad/v1/chat/completions"
#
#async def extract_LMStudio(prompt: str, text: str, model: str = "openai/gpt-oss-20b"):
#    headers = {
#        "Content-Type": "application/json"
#    }
#
#    payload = {
#        "model": model,
#        "messages": [
#            {"role": "system", "content": prompt},
#            {"role": "user", "content": text}
#        ],
#        "temperature": 0.0,
#    }
#
#    async with httpx.AsyncClient() as client:
#        response = await client.post(LMSTUDIO_API_URL, headers=headers, json=payload)
#        response.raise_for_status()
#        data = response.json()
#        return data['choices'][0]['message']['content']
#
