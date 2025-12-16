# api.py
from fastapi import FastAPI
import asyncio
from blacklist_checker import scan_ip

app = FastAPI(title="DNSBL Scanner API")

@app.get("/scan/{ip}")
async def scan(ip: str):
    return await scan_ip(ip)
