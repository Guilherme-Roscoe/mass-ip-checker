import time
from rich.console import Console
from rich.spinner import Spinner
from rich.panel import Panel
import asyncio
from blacklist_checker import scan_ip, export_csv, export_json

ip_list_text = open("ip_list.txt" , "r").read()
ip_list = ip_list_text.splitlines()

ip_limpos = []
todos_ip = {}

inicio = time.time()

console = Console()


for ip in ip_list:

    with console.status(f"[bold green] Checking: {ip} "):
        data = asyncio.run(scan_ip(ip))

    # Don't show the RBLs Panel if check only one address
    if len(ip_list) == 1:
        log_text = '\n'.join([f"{r['blacklist']:40} {r['status']:12} {r['time']:15}s" for r in data['results']])
        
        console.print(
            Panel(
                log_text,
                title="Tested RBLs",
                border_style="green"
            )
        )

    #for r in data["results"]:
    #    print(f"{r['blacklist']:45} {r['status']:12} {r['time']}s")

    listadas = [ l['blacklist'] for l in data['listed_rbl']]

    #register clean IP addresses
    if int(data['listed_count']) == 0:
        ip_limpos.append(ip)

    console.print(f"[bold green]\nIP: {data['ip']}\nRisco: {data['risk']}\nListagens: {data['listed_count']}[/bold green][bold red]\n{' | '.join(listadas)}\n\n[/bold red]")

fim = time.time()
tempo_exec = fim - inicio
if len(ip_list) > 1:
    console.print(f"[bold green]Checked addresses: {len(ip_list)}\nClean IP addresses: {len(ip_limpos)}\nExecution time: {tempo_exec:.2f}[/bold green]")
