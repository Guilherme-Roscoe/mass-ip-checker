import time
from rich.console import Console
from rich.spinner import Spinner

ip_list_text = open("ip_list.txt" , "r").read()
ip_list = ip_list_text.splitlines()

ip_limpos = []

inicio = time.time()

console = Console()

