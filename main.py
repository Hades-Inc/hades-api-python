import os
import random

from supabase import create_client, Client
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv("./.env.local")

app = FastAPI()

supabase: Client = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY"),
)


@app.get("/")
def api_status():
    return {"success": True}


@app.post("/flip")
def submit_coinflip(username: str = "unknown"):
    result = "heads" if random.randint(1, 2) == 1 else "tails"

    data, count = supabase.table('coinflips').insert({
        "username": username,
        "result": result,
    }).execute()
    return data
