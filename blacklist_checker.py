import asyncio
import dns.asyncresolver
import dns.resolver
import time
import csv
import json

BLACKLISTS = [
    "b.barracudacentral.org",
    "bl.score.senderscore.com",
    "bl.spamcannibal.org",
    "bl.spamcop.net",
    "bl.mailspike.net",
    "blacklist.woody.ch",
    "bogons.cymru.com",
    "cbl.abuseat.org",
    "cdl.anti-spam.org.cn",
    "dnsbl-1.uceprotect.net",
    "dnsbl-2.uceprotect.net",
    "dnsbl-3.uceprotect.net",
    "dnsbl.abuse.ch",
    "dnsbl.cyberlogic.net",
    "dnsbl.dronebl.org",
    "dnsbl.inps.de",
    "dnsbl.sorbs.net",
    "dnsbl.spfbl.net",
    "drone.abuse.ch",
    "duinv.aupads.org",
    "dyna.spamrats.com",
    "dynip.rothen.com",
    "http.dnsbl.sorbs.net",
    "images.rbl.msrbl.net",
    "ips.backscatterer.org",
    "ix.dnsbl.manitu.net",
    "korea.services.net",
    "misc.dnsbl.sorbs.net",
    "noptr.spamrats.com",
    "ohps.dnsbl.net.au",
    "omrs.dnsbl.net.au",
    "orvedb.aupads.org",
    "osps.dnsbl.net.au",
    "osrs.dnsbl.net.au",
    "owfs.dnsbl.net.au",
    "owps.dnsbl.net.au",
    "pbl.spamhaus.org",
    "phishing.rbl.msrbl.net",
    "probes.dnsbl.net.au",
    "proxy.bl.gweep.ca",
    "proxy.block.transip.nl",
    "psbl.surriel.com",
    "rbl.interserver.net",
    "rdts.dnsbl.net.au",
    "relays.bl.gweep.ca",
    "relays.nether.net",
    "residential.block.transip.nl",
    "ricn.dnsbl.net.au",
    "rmst.dnsbl.net.au",
    "short.rbl.jp",
    "singular.ttk.pte.hu",
    "smtp.dnsbl.sorbs.net",
    "socks.dnsbl.sorbs.net",
    "spam.abuse.ch",
    "spam.dnsbl.sorbs.net",
    "spam.rbl.msrbl.net",
    "spam.spamrats.com",
    "spamrbl.imp.ch",
    "t3direct.dnsbl.net.au",
    "tor.dnsbl.sectoor.de",
    "torserver.tor.dnsbl.sectoor.de",
    "ubl.lashback.com",
    "ubl.unsubscore.com",
    "virus.rbl.jp",
    "virus.rbl.msrbl.net",
    "web.dnsbl.sorbs.net",
    "wormrbl.imp.ch",
    "xbl.spamhaus.org",
    "zen.spamhaus.org",
    "zombie.dnsbl.sorbs.net",
    "access.redhawk.org"
]

def reverse_ip(ip):
    return ".".join(reversed(ip.split(".")))

def risk_level(count):
    if count == 0:
        return "BAIXO"
    elif count <= 2:
        return "MÉDIO"
    elif count <= 5:
        return "ALTO"
    return "CRÍTICO"

async def check_dnsbl(ip, blacklist):
    resolver = dns.asyncresolver.Resolver()
    resolver.timeout = 3
    resolver.lifetime = 3

    query = f"{reverse_ip(ip)}.{blacklist}"
    start = time.time()

    try:
        await resolver.resolve(query, "A")
        return {"blacklist": blacklist, "status": "LISTADO", "time": round(time.time() - start, 2)}
    except dns.resolver.NXDOMAIN:
        return {"blacklist": blacklist, "status": "NÃO LISTADO", "time": round(time.time() - start, 2)}
    except Exception:
        return {"blacklist": blacklist, "status": "ERRO", "time": round(time.time() - start, 2)}

async def scan_ip(ip):
    tasks = [check_dnsbl(ip, bl) for bl in BLACKLISTS]
    results = await asyncio.gather(*tasks)

    listed = [r for r in results if r["status"] == "LISTADO"]

    return {
        "ip": ip,
        "listed_count": len(listed),
        "risk": risk_level(len(listed)),
        "results": results,
        "listed_rbl": listed
    }

def export_csv(data, filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Blacklist", "Status", "Time"])
        for r in data["results"]:
            writer.writerow([r["blacklist"], r["status"], r["time"]])

def export_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
