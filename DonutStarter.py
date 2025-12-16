import time
from rich.console import Console
from rich.spinner import Spinner
import asyncio
from blacklist_checker import scan_ip, export_csv, export_json

ip_list_text = open("ip_list.txt" , "r").read()
ip_list = ip_list_text.splitlines()

ip_limpos = []

inicio = time.time()

console = Console()

for ip in ip_list:
    data = asyncio.run(scan_ip(ip))

    for r in data["results"]:
        print(f"{r['blacklist']:45} {r['status']:12} {r['time']}s")

    print(f"\nIP: {data['ip']}")
    print(f"Listagens: {data['listed_count']}")
    print(f"Risco: {data['risk']}\n")
