# web.py
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import asyncio
from blacklist_checker import scan_ip

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <form method="post">
        <input name="ip" placeholder="Digite o IP"/>
        <button>Verificar</button>
    </form>
    """

@app.post("/", response_class=HTMLResponse)
async def result(ip: str = Form(...)):
    data = await scan_ip(ip)
    rows = "".join(
        f"<tr><td>{r['blacklist']}</td><td>{r['status']}</td><td>{r['time']}s</td></tr>"
        for r in data["results"]
    )
    return f"""
    <h2>IP: {ip}</h2>
    <h3>Risco: {data['risk']}</h3>
    <table border=1>
        <tr><th>Blacklist</th><th>Status</th><th>Tempo</th></tr>
        {rows}
    </table>
    """
