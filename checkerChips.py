import requests
from bs4 import BeautifulSoup

ip_list_text = open("ip_list.txt" , "r").read()
ip_list = ip_list_text.splitlines()

for ip in ip_list:
    print("Checando:",ip)

    #requisição ao buscador
    check = requests.get(f"https://buscaip.com.br/blacklist_check/?ip={ip}")
    check_page = check.text

    #separação do HTML
    soup = BeautifulSoup(check_page, "html.parser")
    blacklists_count = soup.select_one("div.resultado__blacklist.bg-danger p b:last-child").text

    #lista blacklists q contém o IP
    dominios_listados = []
    for row in soup.select("tbody tr"):
        dominio = row.find_all("td")[0].text.strip()
        status = row.find("span").text.strip()

        if status == "Listado":
            dominios_listados.append(dominio)

    dominios_listados_form = '\n'.join(dominios_listados)

    print("\nEste IP está listado em",blacklists_count,"blacklists:\n\n",dominios_listados_form)
    print("="*20)
