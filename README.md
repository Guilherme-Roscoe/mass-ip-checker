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

1. **Python 3.x**: This code was developed for Python 3.10+, so please install the latest version of Python.
2. **⬇️📦 Installing dependencies**:
   - `dnspython` — To perform DNS queries.
   - `fastapi` and `uvicorn` — For REST API and web server.
  
   
   Navigate to the project folder and run:

   `pip install -r requirements.txt`

---
### 🧑‍💻 Contributions

  If you'd like to contribute to the project, feel free to create a pull request! Suggestions for improvements are always welcome.

---
### 🧯 Common Problems

  ❌ ModuleNotFoundError: dns
  
  This means the dnspython library is not installed. To fix this, run:
  
  `pip install dnspython`
  
  ❌ Timeout on multiple lists
  
  Don't worry about it. That problem was resolved in the latest version; now the bot retries lists after a timeout.

---
### 🎁 Future Improvements

  - Dockerization of the project
  
  - API authentication (to prevent abuse)
  
  - Caching for fast results
  
  - Interactive dashboard with React or similar
  
  - Logs to track executions
  
  - .exe version for Windows

###🔑 License

This project is licensed under the MIT License.
