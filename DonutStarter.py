import time
from rich.console import Console
from rich.spinner import Spinner
from rich.text import Text
from rich.panel import Panel
import asyncio
from blacklist_checker import scan_ip, donut_print, export_csv, export_json

#Define a list with IPs to be checked
ip_list_text = open("ip_list.txt" , "r").read()
ip_list = ip_list_text.splitlines()

#List to separe clean IP
ip_limpos = []
todos_ip = []

inicio = time.time() #calc exec time

console = Console()
console.rule("[magenta] DONUTS IP CHECKER", style="hot_pink")
donut_print(console)

#Starts checking
for ip in ip_list:
    inicio_l = time.time()
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

    fim_l = time.time()
    tempo_exec_l = fim_l-inicio_l
    console.print(f"[bold green]Check time: {tempo_exec_l:.2f}[/bold green]")
    #for r in data["results"]:
    #    print(f"{r['blacklist']:45} {r['status']:12} {r['time']}s")

    listadas = [ l['blacklist'] for l in data['listed_rbl']] #name of RBLs found

    ip_info = {
        "ip": ip,
        "rbl_n": data['listed_count'],
        "risco": data["risk"],
        "listas": listadas
    }
    todos_ip.append(ip_info)

    #register clean IP addresses
    if int(data['listed_count']) == 0:
        ip_limpos.append(ip_info)

    console.print(f"[bold green]IP: {data['ip']}\nRisco: {data['risk']}\nListagens: {data['listed_count']}[/bold green][bold red]\n{' | '.join(listadas)}\n\n[/bold red]")

fim = time.time()
tempo_exec = fim - inicio
if len(ip_list) > 1:
    console.print(f"[bold green]Execution time: {tempo_exec:.2f}\nChecked addresses: {len(ip_list)}\nClean IP addresses: {len(ip_limpos)}[/bold green]")

resultado_text = Text(f"\n{'IP ADDRESS':45} {'BLACKLISTS COUNT':30} {'RBLs LISTED':10}\n",style="magenta")
for ipr in todos_ip:
    if int(ipr["rbl_n"]) < 4:
        resultado_text.append(f"{ipr["ip"]:45} {ipr["rbl_n"]:10} {"lista.tal.spam.sla":10}", style="green")

infos_result = Panel(
    resultado_text,
    title="DONUT RESULT",
    border_style="magenta"
)
console.print(infos_result)

# CLOCAR INFOS SOBRE CADA IP NA LISTA todos_ips PARA O LOG FINAL
