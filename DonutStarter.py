import time
import asyncio
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from blacklist_checker import scan_ip, donut_print

# ===============================
# CONFIG
# ===============================
MAX_CONCURRENT = 50  # limite seguro para DNS
IP_LIST_FILE = "ip_list.txt"

# ===============================
# SETUP
# ===============================
console = Console()

ip_list = open(IP_LIST_FILE).read().splitlines()
ip_limpos = []
todos_ip = []

inicio = time.time()

console.rule("[magenta] DONUTS IP CHECKER", style="hot_pink")
donut_print(console)

# ===============================
# ASYNC WORKER
# ===============================
sem = asyncio.Semaphore(MAX_CONCURRENT)

async def scan_ip_safe(ip: str):
    async with sem:
        inicio_l = time.time()
        data = await scan_ip(ip)
        tempo = time.time() - inicio_l
        return ip, data, tempo

# ===============================
# MAIN ASYNC RUNNER
# ===============================
async def run_all_ips():
    tasks = [scan_ip_safe(ip) for ip in ip_list]

    with console.status("[bold green]Checking all IPs asynchronously..."):
        results = await asyncio.gather(*tasks)

    for ip, data, tempo_exec_l in results:

        listadas = [l["blacklist"] for l in data["listed_rbl"]]

        ip_info = {
            "ip": ip,
            "rbl_n": data["listed_count"],
            "risco": data["risk"],
            "listas": listadas
        }

        todos_ip.append(ip_info)

        if int(data["listed_count"]) == 0:
            ip_limpos.append(ip_info)

        #console.print(
        #    f"[bold green]IP: {ip}"
        #    f"\nRisco: {data['risk']}"
        #    f"\nListagens: {data['listed_count']}"
        #    f"\nTempo: {tempo_exec_l:.2f}s[/bold green]"
        #)

        #if listadas:
        #    console.print(f"[bold red]{' | '.join(listadas)}[/bold red]\n")

# ===============================
# EXECUTION
# ===============================
asyncio.run(run_all_ips())

# ===============================
# FINAL STATS
# ===============================
fim = time.time()
tempo_exec = fim - inicio

console.print(
    f"[bold green]Execution time: {tempo_exec:.2f}s"
    f"\nChecked addresses: {len(ip_list)}"
    f"\nClean IP addresses: {len(ip_limpos)}[/bold green]"
)

# ===============================
# RESULT TABLE
# ===============================
infos_result = Table(
    title="DONUT RESULT",
    title_style="bold magenta",
    style="magenta"
)

infos_result.add_column("IP ADDRESS")
infos_result.add_column("RBLs COUNT")
infos_result.add_column("RISK")
infos_result.add_column("RBLs LISTED")

for ipr in todos_ip:
    infos_result.add_row(
        ipr["ip"],
        str(ipr["rbl_n"]),
        ipr["risco"],
        " | ".join(ipr["listas"]) or "-"
    )

console.print(infos_result)
