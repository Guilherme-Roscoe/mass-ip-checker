import requests
from bs4 import BeautifulSoup
import time
from rich.console import Console
from rich.spinner import Spinner

ip_list_text = open("ip_list.txt" , "r").read()
ip_list = ip_list_text.splitlines()

ip_limpos = []

inicio = time.time()

console = Console()

for ip in ip_list:
    with console.status(f"[bold green] Checking: {ip} "):
        #requisição ao buscador
        check = requests.get(f"https://buscaip.com.br/blacklist_check/?ip={ip}")
    check_page = check.text

    #separação do HTML
    soup = BeautifulSoup(check_page, "html.parser")
    blacklists_count = soup.select_one("div.resultado__blacklist.bg-danger p b:last-child").text

    if int(blacklists_count) == 0:
        ip_limpos.append(ip)

    #lista blacklists q contém o IP
    dominios_listados = []
    for row in soup.select("tbody tr"):
        dominio = row.find_all("td")[0].text.strip()
        status = row.find("span").text.strip()

        if status == "Listado":
            dominios_listados.append(dominio)

    dominios_listados_form = '\n'.join(dominios_listados)

    print("\n",ip,"is listed in",blacklists_count,"blacklists:\n\n",dominios_listados_form)
    print("="*20)

fim = time.time()

tempo_execucao = fim - inicio
print(f"Checking is over\n Execution time: {tempo_execucao:.2f} sec\n")

print("The following IP addresses were not found on any blacklist:\n", '\n'.join(ip_limpos), "\n--------\n")
