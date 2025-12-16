# cli.py
import argparse
import asyncio
from blacklist_checker import scan_ip, export_csv, export_json

parser = argparse.ArgumentParser(description="DNSBL Scanner Profissional")
parser.add_argument("ip", help="IP para verificar")
parser.add_argument("--csv", help="Exportar CSV")
parser.add_argument("--json", help="Exportar JSON")

args = parser.parse_args()
data = asyncio.run(scan_ip(args.ip))

print(f"\nIP: {data['ip']}")
print(f"Listagens: {data['listed_count']}")
print(f"Risco: {data['risk']}\n")

for r in data["results"]:
    print(f"{r['blacklist']:45} {r['status']:12} {r['time']}s")

if args.csv:
    export_csv(data, args.csv)

if args.json:
    export_json(data, args.json)
