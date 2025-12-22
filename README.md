# 🌐 Asynchronous Mass IP Blacklist Checker

#### Python application for bulk checking if IPs are on a blacklist.
---
This is a **DNSBL (Blacklist) scanner** to check if an IP address is listed on various blacklists. The program can be run in several ways, including a **professional CLI**, a **REST API**, and a simple **web interface**. The system also allows **exporting results in CSV or JSON format** and classifies the risk according to the number of lists in which the IP was found.

- ⚡ Asynchronous (fast) execution
- 🖥️ Professional CLI
- 🌐 REST API (FastAPI)
- 🧾 Simple web interface
- 📄 CSV and JSON export
- 🧠 Automatic risk classification
  
---
## 📂 Create the project folder

Open the terminal or PowerShell and create a directory for the project:

`mkdir dnsbl_scanner`
`cd dnsbl_scanner`

---
## 📦 Baixando pré-requisitos

1. **Python 3.x**: O código foi desenvolvido para Python 3.10+, então, por favor, instale a versão mais recente do Python.
2. **⬇️📦 Instalação das Dependências**:
   - `dnspython` — Para realizar consultas DNS.
   - `fastapi` e `uvicorn` — Para API REST e servidor web.
  
   
   Entre na pasta do projeto e execute:

   `pip install -r requirements.txt`

---
### 🧑‍💻 Contribuições

Se você quiser contribuir com o projeto, fique à vontade para criar uma pull request! Sugestões de melhorias são sempre bem-vindas.

---
### 🧯 Problemas Comuns

❌ ModuleNotFoundError: dns

Isso significa que a biblioteca dnspython não está instalada. Para corrigir, execute:

`pip install dnspython`

❌ Timeout em várias listas

É normal que algumas listas negras tenham tempo de resposta alto ou até bloqueiem consultas. Isso pode ocorrer com listas populares como Spamhaus, por exemplo.

---
### 🎁 Melhorias Futuras

 - Dockerização do projeto

 - Autenticação para API (para evitar abuso)

 - Cache para resultados rápidos

 - Dashboard interativo com React ou similar

 - Logs para rastrear execuções

 - Versão em .exe para Windows

🔑 Licença

Este projeto está licenciado sob a MIT License.
