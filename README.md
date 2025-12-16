# DNSBL Scanner

Este é um **scanner de DNSBL** (Blacklists) para verificar se um endereço IP está listado em diversas listas negras. O programa pode ser executado de várias formas, incluindo uma **CLI profissional**, uma **API REST**, e uma **interface Web** simples. O sistema também permite a **exportação de resultados em CSV ou JSON** e classifica o risco de acordo com o número de listas em que o IP foi encontrado.

- ⚡ Execução assíncrona (rápida)
- 🖥️ CLI profissional
- 🌐 API REST (FastAPI)
- 🧾 Interface Web simples
- 📄 Exportação CSV e JSON
- 🧠 Classificação automática de risco


## 📦 Pré-requisitos

1. **Python 3.x**: O código foi desenvolvido para Python 3.10+, então, por favor, instale a versão mais recente do Python.
2. **Instalar dependências**:
   - `dnspython` — Para realizar consultas DNS.
   - `fastapi` e `uvicorn` — Para API REST e servidor web.

---

## 🚀 Rodando o Programa

### 📂 Criar a pasta do projeto

Abra o terminal ou PowerShell e crie um diretório para o projeto:

mkdir dnsbl_scanner
cd dnsbl_scanner
# DNSBL Scanner

Este é um **scanner de DNSBL** (Blacklists) para verificar se um endereço IP está listado em diversas listas negras. O programa pode ser executado de várias formas, incluindo uma **CLI profissional**, uma **API REST**, e uma **interface Web** simples. O sistema também permite a **exportação de resultados em CSV ou JSON** e classifica o risco de acordo com o número de listas em que o IP foi encontrado.

## 📦 Pré-requisitos

1. **Python 3.x**: O código foi desenvolvido para Python 3.10+, então, por favor, instale a versão mais recente do Python.
2. **Instalar dependências**:
   - `dnspython` — Para realizar consultas DNS.
   - `fastapi` e `uvicorn` — Para API REST e servidor web.
  
   ####⬇️📦 Instalação das Dependências
   Entre na pasta do projeto e execute:

   `pip install dnspython fastapi uvicorn`

---

## 🚀 Rodando o Programa

Você pode rodar o programa de diferentes formas:

####1 Modo CLI (linha de comando)

Para rodar o programa no terminal:

`python cli.py 154.6.126.49`


Você também pode exportar os resultados para CSV ou JSON:

`python cli.py 154.6.126.49 --csv resultado.csv --json resultado.json`

---
####2 Modo API REST

Para rodar a API REST, execute:

`uvicorn api:app --reload`


Acesse a API através de:

`http://localhost:8000/scan/154.6.126.49`

---
###3 Modo Interface Web

Para rodar a interface Web simples, execute:

`uvicorn web:app --reload`

Abra no navegador em:

`http://localhost:8000`


Digite o IP e clique Verificar.

###⚙️ Como Funciona

Consultas DNS: O programa consulta uma série de listas negras (DNSBLs) para verificar se o IP está listado.

Classificação de Risco: O risco é classificado de acordo com o número de listas em que o IP aparece:

0 Listagens: Risco BAIXO

1-2 Listagens: Risco MÉDIO

3-5 Listagens: Risco ALTO

6+ Listagens: Risco CRÍTICO

Exportação: Você pode exportar os resultados da verificação em CSV ou JSON.

---
###🧑‍💻 Contribuições

Se você quiser contribuir com o projeto, fique à vontade para criar uma pull request! Sugestões de melhorias são sempre bem-vindas.

---
###🧯 Problemas Comuns

❌ ModuleNotFoundError: dns

Isso significa que a biblioteca dnspython não está instalada. Para corrigir, execute:

`pip install dnspython`

❌ Timeout em várias listas

É normal que algumas listas negras tenham tempo de resposta alto ou até bloqueiem consultas. Isso pode ocorrer com listas populares como Spamhaus, por exemplo.

---
###🎁 Melhorias Futuras

 - Dockerização do projeto

 - Autenticação para API (para evitar abuso)

 - Cache para resultados rápidos

 - Dashboard interativo com React ou similar

 - Logs para rastrear execuções

 - Versão em .exe para Windows

🔑 Licença

Este projeto está licenciado sob a MIT License.
