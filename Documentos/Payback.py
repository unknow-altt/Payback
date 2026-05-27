#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 ██████╗  █████╗ ██╗   ██╗██████╗  █████╗  ██████╗██╗  ██╗
 ██╔══██╗██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
 ██████╔╝███████║ ╚████╔╝ ██████╔╝███████║██║     █████╔╝ 
 ██╔═══╝ ██╔══██║  ╚██╔╝  ██╔══██╗██╔══██║██║     ██╔═██╗ 
 ██║     ██║  ██║   ██║   ██████╔╝██║  ██║╚██████╗██║  ██╗
 ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                    by dasis
"""

import os
import sys
import time
import random
import string

# ─── COLORES ANSI ────────────────────────────────────────────
RED   = '\033[91m'
GREEN = '\033[92m'
YELLOW= '\033[93m'
CYAN  = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD  = '\033[1m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.02, color=WHITE):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fake_ip():
    return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"

def fake_loading(texto, seg=2):
    print(CYAN + f"[*] {texto}", end='', flush=True)
    for _ in range(seg * 2):
        time.sleep(0.5)
        print('.', end='', flush=True)
    print(RESET)
    print(GREEN + "[✔] Completado.\n" + RESET)
    time.sleep(0.5)

def progress_bar(total, mensaje="Progreso"):
    print(YELLOW + f"[*] {mensaje}: ", end='')
    for i in range(total):
        time.sleep(0.05)
        p = int((i+1)/total*20)
        bar = '█'*p + '░'*(20-p)
        print(f"\r{YELLOW}[*] {mensaje}: [{bar}] {i+1}/{total}", end='', flush=True)
    print(RESET)
    print(GREEN + "[✔] Finalizado.\n" + RESET)

def banner():
    clear()
    print(RED + BOLD + r"""
 ██████╗  █████╗ ██╗   ██╗██████╗  █████╗  ██████╗██╗  ██╗
 ██╔══██╗██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
 ██████╔╝███████║ ╚████╔╝ ██████╔╝███████║██║     █████╔╝ 
 ██╔═══╝ ██╔══██║  ╚██╔╝  ██╔══██╗██╔══██║██║     ██╔═██╗ 
 ██║     ██║  ██║   ██║   ██████╔╝██║  ██║╚██████╗██║  ██╗
 ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
""" + RESET)
    print(YELLOW + BOLD + "\t[!] Herramienta de Auditoría y Pentest" + RESET)
    print(YELLOW + "\t[!] v5.1 | Linux CachyOS | by dasis" + RESET)
    print(RED + "─"*60 + RESET)

def disclaimer():
    slow_print("\n⚠  ADVERTENCIA LEGAL ⚠", 0.03, RED)
    slow_print("Esta herramienta es exclusivamente para auditorías de seguridad en sistemas propios o con autorización explícita.", 0.02, YELLOW)
    slow_print("El uso indebido contra sistemas sin permiso es ILEGAL y puede acarrear graves consecuencias legales.", 0.02, RED)
    slow_print("El creador NO asume ninguna responsabilidad por el uso que le des. Bajo tu propio riesgo.\n", 0.02, RED)
    res = input(WHITE + "¿Entiendes y aceptas estos términos? (s/n): " + RESET).lower()
    if res != 's':
        print(RED + "\n[!] Acceso denegado. Saliendo..." + RESET)
        sys.exit(0)
    clear()
    banner()
    print(GREEN + "[✔] Módulos cargados correctamente.\n" + RESET)
    time.sleep(1)

def menu():
    print(CYAN + BOLD + "╔══════════════════════════════════════╗" + RESET)
    print(CYAN + BOLD + "║           MENÚ PRINCIPAL            ║" + RESET)
    print(CYAN + BOLD + "╠══════════════════════════════════════╣" + RESET)
    opciones = [
        "1.  Doxear objetivo               ",
        "2.  Escanear puertos              ",
        "3.  Ataque DDoS                   ",
        "4.  Generar página phishing       ",
        "5.  Sniffer de red                ",
        "6.  Keylogger remoto              ",
        "7.  Generador tarjetas CC         ",
        "8.  Enviar SMS spoof              ",
        "9.  Crackear hash                 ",
        "10. Geolocalizar IP               ",
        "11. Discord Token Grabber         ",
        "12. Spam Webhook Discord          ",
        "13. Instagram Scraper             ",
        "14. Facebook Account Checker      ",
        "15. Robar contraseñas WiFi        ",
        "16. Generador de payloads         ",
        "17. Escáner de subdominios        ",
        "18. Fuerza bruta SSH              ",
        "19. SQL Injection scanner         ",
        "20. BIN Checker (tarjetas)        ",
        "21. Salir                         "
    ]
    for op in opciones:
        print(CYAN + "║ " + WHITE + op + CYAN + "║" + RESET)
    print(CYAN + BOLD + "╚══════════════════════════════════════╝" + RESET)

# ─── FUNCIONES DE HERRAMIENTAS ───────────────────────────────

def doxear():
    clear()
    banner()
    print(RED + BOLD + "[+] DOXEO DE OBJETIVO\n" + RESET)
    nombre = input(WHITE + "Nombre/alias: " + RESET) or "objetivo"
    fake_loading("Buscando en bases de datos filtradas")
    print(YELLOW + "[!] Resultados obtenidos:" + RESET)
    info = {
        "Nombre completo": f"{nombre.capitalize()} Martínez Rodríguez",
        "Dirección": f"Calle Falsa {random.randint(100,999)}, Col. Centro, CDMX",
        "Teléfono": f"+52 55 {random.randint(1000,9999)} {random.randint(1000,9999)}",
        "Correo": f"{nombre.lower()}{random.randint(1,99)}@protonmail.com",
        "IP": fake_ip(),
        "Redes sociales": f"fb.com/{nombre}.{random.randint(10,99)}, ig/@{nombre}_x"
    }
    for k, v in info.items():
        print(f"{WHITE}{k}: {GREEN}{v}{RESET}")
        time.sleep(0.2)
    print(RED + "\n[!] Datos exportados a /tmp/dox_{nombre}.csv" + RESET)
    input(WHITE + "\nPresiona Enter para volver..." + RESET)

def escanear_puertos():
    clear()
    banner()
    print(RED + BOLD + "[+] ESCANEO DE PUERTOS\n" + RESET)
    ip = input(WHITE + "IP objetivo: " + RESET) or fake_ip()
    fake_loading(f"Iniciando escaneo SYN en {ip}")
    puertos = [21,22,25,80,443,3306,8080,8443,9000,2222]
    print(YELLOW + f"Resultados para {ip}:" + RESET)
    for p in puertos:
        estado = random.choice(["ABIERTO", "CERRADO", "FILTRADO"])
        color = GREEN if estado == "ABIERTO" else RED
        print(f"  {WHITE}Puerto {p}: {color}{estado}{RESET}")
        time.sleep(0.2)
    input(WHITE + "\nPresiona Enter para volver..." + RESET)

def ataque_ddos():
    clear()
    banner()
    print(RED + BOLD + "[+] ATAQUE DDoS\n" + RESET)
    target = input(WHITE + "IP/URL objetivo: " + RESET) or "http://victima.com"
    print(YELLOW + f"\n[!] Lanzando botnet contra {target}..." + RESET)
    progress_bar(50, "Enviando paquetes UDP")
    print(RED + "[✔] Ataque detenido manualmente." + RESET)
    input(WHITE + "\nPresiona Enter para volver..." + RESET)

def phishing():
    clear()
    banner()
    print(RED + BOLD + "[+] GENERADOR DE PÁGINA PHISHING\n" + RESET)
    sitio = input(WHITE + "Sitio a clonar (ej. facebook, instagram): " + RESET)
    fake_loading(f"Clonando {sitio}.com")
    url_falsa = f"http://{sitio}-verify.{random.randint(1000,9999)}.cf/login.php"
    print(GREEN + f"[✔] Página generada: {url_falsa}" + RESET)
    print(YELLOW + "[!] Envía este enlace al objetivo para capturar credenciales." + RESET)
    input(WHITE + "\nPresiona Enter para volver..." + RESET)

def sniffer():
    clear()
    banner()
    print(RED + BOLD + "[+] SNIFFER DE RED\n" + RESET)
    fake_loading("Poniendo interfaz en modo monitor")
    for _ in range(12):
        ip_src = fake_ip()
        ip_dst = fake_ip()
        print(f"{CYAN}[>] {ip_src} -> {ip_dst} | HTTP GET /login.php{random.choice(['?user=admin&pass=1234','?email=test@mail.com&pass=test123'])} {RESET}")
        time.sleep(0.3)
    input(WHITE + "\nPresiona Enter para volver..." + RESET)

def keylogger():
    clear()
    banner()
    print(RED + BOLD + "[+] KEYLOGGER REMOTO\n" + RESET)
    fake_loading("Desplegando payload en el cliente")
    print(YELLOW + "[!] Capturando teclas de la víctima:" + RESET)
    teclas = "usuario: admin@gmail.com | contraseña: P@ssw0rd123 | Tarjeta: 4539 1234 5678 9012".split('|')
    for t in teclas:
        print(f"  {GREEN}{t.strip()}{RESET}")
        time.sleep(0.7)
    input(WHITE + "\nPresiona Enter para volver..." + RESET)

def gen_cc():
    clear()
    banner()
    print(RED + BOLD + "[+] GENERADOR DE TARJETAS DE CRÉDITO\n" + RESET)
    for _ in range(4):
        num = ' '.join([''.join(random.choices(string.digits, k=4)) for _ in range(4)])
        mes = str(random.randint(1,12)).zfill(2)
        anio = str(random.randint(2025,2030))
        cvv = ''.join(random.choices(string.digits, k=3))
        print(f"{GREEN}VISA: {num} | EXP: {mes}/{anio} | CVV: {cvv}{RESET}")
        time.sleep(0.5)
    input(WHITE + "\nPresiona Enter para volver..." + RESET)

def sms_spoof():
    clear()
    banner()
    print(RED + BOLD + "[+] ENVÍO DE SMS FALSIFICADO\n" + RESET)
    destino = input(WHITE + "Número destino: +" + RESET)
    mensaje = input(WHITE + "Mensaje: " + RESET)
    fake_loading("Conectando a pasarela SMS anónima")
    print(GREEN + f"[✔] SMS enviado correctamente a +{destino}: " + RESET)
    print(f"    \"{mensaje}\"")
    input(WHITE + "\nPresiona Enter para volver..." + RESET)

def crack_hash():
    clear()
    banner()
    print(RED + BOLD + "[+] CRACKEO DE HASH\n" + RESET)
    hash_input = input(WHITE + "Hash (MD5/SHA1): " + RESET) or "5f4dcc3b5aa765d61d8327deb882cf99"
    fake_loading("Iniciando ataque de diccionario")
    progress_bar(35, "Probando contraseñas")
    passwd = random.choice(["password", "123456", "admin", "qwerty", "letmein", "iloveyou"])
    print(GREEN + f"[✔] Contraseña encontrada: {passwd}" + RESET)
    input(WHITE + "\nPresiona Enter para volver..." + RESET)

def geolocalizar():
    clear()
    banner()
    print(RED + BOLD + "[+] GEOLOCALIZACIÓN DE IP\n" + RESET)
    ip = input(WHITE + "IP a localizar: " + RESET) or fake_ip()
    fake_loading("Consultando base de datos GeoIP")
    print(f"{WHITE}IP: {GREEN}{ip}{RESET}")
    print(f"{WHITE}País: {GREEN}{random.choice(['México','Colombia','España','Argentina','Chile'])}{RESET}")
    print(f"{WHITE}Ciudad: {GREEN}{random.choice(['Ciudad de México','Bogotá','Madrid','Buenos Aires','Santiago'])}{RESET}")
    print(f"{WHITE}ISP: {GREEN}{random.choice(['Telmex','Movistar','Claro','Personal','VTR'])}{RESET}")
    print(f"{WHITE}Proxy/VPN: {GREEN}{random.choice(['No detectado','VPN NordVPN','Proxy anónimo'])}{RESET}")
    input(WHITE + "\nPresiona Enter para volver..." + RESET)

def discord_token_grabber():
    clear()
    banner()
    print(RED + BOLD + "[+] DISCORD TOKEN GRABBER\n" + RESET)
    fake_loading("Escaneando archivos locales de Discord")
    tokens = []
    for i in range(3):
        token = ''.join(random.choices(string.ascii_letters + string.digits + "._-", k=59)) + "." + ''.join(random.choices(string.ascii_letters + string.digits, k=27)) + "." + ''.join(random.choices(string.ascii_letters + string.digits + "_", k=38))
        tokens.append(token)
    print(GREEN + "[✔] Tokens encontrados:" + RESET)
    for t in tokens:
        print(f"  {WHITE}{t[:50]}...{RESET}")
        time.sleep(0.5)
    print(RED + "\n[!] Tokens exportados a tokens.txt" + RESET)
    input(WHITE + "\nPresiona Enter para volver..." + RESET)

def discord_webhook_spam():
    clear()
    banner()
    print(RED + BOLD + "[+] SPAM WEBHOOK DISCORD\n" + RESET)
    webhook = input(WHITE + "Webhook URL: " + RESET)
    mensaje = input(WHITE + "Mensaje a spamear: " + RESET)
    veces = input(WHITE + "Cantidad (1-100): " + RESET) or "10"
    fake_loading("Iniciando envío masivo")
    progress_bar(int(veces), "Mensajes enviados")
    print(GREEN + f"[✔] Se enviaron {veces} mensajes al webhook." + RESET)
    input(WHITE + "\nPresiona Enter para volver..." + RESET)

def instagram_scraper():
    clear()
    banner()
    print(RED + BOLD + "[+] INSTAGRAM SCRAPER\n" + RESET)
    user = input(WHITE + "Usuario a investigar: @" + RESET)
    fake_loading(f"Extrayendo datos de @{user}")
    print(f"{WHITE}Usuario: {GREEN}@{user}{RESET}")
    print(f"{WHITE}Nombre completo: {GREEN}{random.choice(['Laura Gómez','Carlos Pérez','Ana Ríos'])}{RESET}")
    print(f"{WHITE}Seguidores: {GREEN}{random.randint(300,5000)}{RESET}")
    print(f"{WHITE}Publicaciones: {GREEN}{random.randint(10,500)}{RESET}")
    print(f"{WHITE}Correo: {GREEN}{user}@hotmail.com{RESET}")
    print(f"{WHITE}Teléfono vinculado: {GREEN}+52 55 {random.randint(1000,9999)} {random.randint(1000,9999)}{RESET}")
    input(WHITE + "\nPresiona Enter para volver..." + RESET)

def facebook_checker():
    clear()
    banner()
    print(RED + BOLD + "[+] FACEBOOK ACCOUNT CHECKER\n" + RESET)
    correo = input(WHITE + "Correo/ID de Facebook: " + RESET)
    fake_loading("Verificando en base de datos")
    existe = random.choice([True, False])
    if existe:
        print(GREEN + "[✔] Cuenta encontrada." + RESET)
        print(f"{WHITE}Nombre: {GREEN}Usuario FB_{random.randint(100,999)}{RESET}")
        print(f"{WHITE}Amigos: {GREEN}{random.randint(50,2000)}{RESET}")
        print(f"{WHITE}Ubicación: {GREEN}{random.choice(['México','España','Argentina'])}{RESET}")
    else:
        print(RED + "[!] No se encontró cuenta con ese correo." + RESET)
    input(WHITE + "\nPresiona Enter para volver..." + RESET)

def wifi_stealer():
    clear()
    banner()
    print(RED + BOLD + "[+] ROBO DE CONTRASEÑAS WIFI\n" + RESET)
    fake_loading("Ejecutando netsh wlan show profiles")
    perfiles = ["INFINITUM-5012","Casa_Alvarez","TP-Link_EXT","Starbucks_WiFi"]
    for p in perfiles:
        clave = ''.join(random.choices(string.ascii_letters+string.digits, k=10))
        print(f"{WHITE}SSID: {GREEN}{p}{WHITE} | Contraseña: {GREEN}{clave}{RESET}")
        time.sleep(0.4)
    input(WHITE + "\nPresiona Enter para volver..." + RESET)

def payload_generator():
    clear()
    banner()
    print(RED + BOLD + "[+] GENERADOR DE PAYLOADS\n" + RESET)
    tipos = ["reverse_shell", "bind_shell", "meterpreter"]
    print(WHITE + "Tipos disponibles:" + RESET)
    for t in tipos:
        print(f"  {GREEN}{t}{RESET}")
    tipo = input(WHITE + "\nElige tipo: " + RESET) or "reverse_shell"
    ip = input(WHITE + "LHOST: " + RESET)
    port = input(WHITE + "LPORT: " + RESET) or "4444"
    fake_loading("Generando payload")
    if tipo == "reverse_shell":
        payload = f"msfvenom -p linux/x86/shell_reverse_tcp LHOST={ip} LPORT={port} -f elf -o shell.elf"
    else:
        payload = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f exe -o payload.exe"
    print(GREEN + f"[✔] Payload generado: {payload}{RESET}")
    input(WHITE + "\nPresiona Enter para volver..." + RESET)

def subdomain_scanner():
    clear()
    banner()
    print(RED + BOLD + "[+] ESCÁNER DE SUBDOMINIOS\n" + RESET)
    dominio = input(WHITE + "Dominio: " + RESET) or "example.com"
    fake_loading(f"Buscando subdominios de {dominio}")
    sub = ["www","mail","ftp","admin","dev","api","shop","blog","test","secure"]
    for s in sub:
        print(f"{GREEN}[+] {s}.{dominio}{WHITE} -> {RESET}{fake_ip()}")
        time.sleep(0.2)
    print(GREEN + f"\n[✔] Total: {len(sub)} subdominios encontrados." + RESET)
    input(WHITE + "\nPresiona Enter para volver..." + RESET)

def ssh_bruteforce():
    clear()
    banner()
    print(RED + BOLD + "[+] FUERZA BRUTA SSH\n" + RESET)
    ip = input(WHITE + "IP objetivo: " + RESET)
    usuario = input(WHITE + "Usuario: " + RESET) or "root"
    fake_loading("Cargando diccionario")
    progress_bar(25, "Probando combinaciones")
    if random.choice([True, False]):
        passwd = random.choice(["admin123","toor","raspberry","password"])
        print(GREEN + f"[✔] ¡Acceso conseguido! {usuario}:{passwd}@{ip}{RESET}")
    else:
        print(RED + "[!] No se encontraron credenciales válidas." + RESET)
    input(WHITE + "\nPresiona Enter para volver..." + RESET)

def sqli_scanner():
    clear()
    banner()
    print(RED + BOLD + "[+] SQL INJECTION SCANNER\n" + RESET)
    url = input(WHITE + "URL objetivo: " + RESET)
    fake_loading("Inyectando payloads")
    resultados = [f"SQLi encontrada en parámetro 'id'", f"Error basado en UNION en 'cat'", "Sin vulnerabilidades detectadas"]
    print(YELLOW + "[*] Resultados:" + RESET)
    for r in resultados[:2]:
        print(f"  {RED}[VULN]{RESET} {r}" if "encontrada" in r or "UNION" in r else f"  {GREEN}[INFO]{RESET} {r}")
        time.sleep(0.7)
    input(WHITE + "\nPresiona Enter para volver..." + RESET)

def bin_checker():
    clear()
    banner()
    print(RED + BOLD + "[+] BIN CHECKER (TARJETAS)\n" + RESET)
    bin_input = input(WHITE + "Ingresa BIN (primeros 6 dígitos): " + RESET) or "453912"
    fake_loading("Consultando base de datos de BIN")
    print(f"{WHITE}BIN: {GREEN}{bin_input}{RESET}")
    print(f"{WHITE}Marca: {GREEN}VISA{random.choice(['',' Gold',' Platinum'])}{RESET}")
    print(f"{WHITE}Entidad: {GREEN}{random.choice(['BBVA','Santander','Banamex'])}{RESET}")
    print(f"{WHITE}País: {GREEN}{random.choice(['México','España','USA'])}{RESET}")
    print(f"{WHITE}Tipo: {GREEN}{random.choice(['Crédito','Débito'])}{RESET}")
    print(f"{WHITE}Nivel: {GREEN}{random.choice(['Classic','Gold','Platinum'])}{RESET}")
    input(WHITE + "\nPresiona Enter para volver..." + RESET)

def main():
    banner()
    disclaimer()
    while True:
        clear()
        banner()
        menu()
        op = input(WHITE + "\n[?] Selecciona una opción: " + RESET)
        if op == '1': doxear()
        elif op == '2': escanear_puertos()
        elif op == '3': ataque_ddos()
        elif op == '4': phishing()
        elif op == '5': sniffer()
        elif op == '6': keylogger()
        elif op == '7': gen_cc()
        elif op == '8': sms_spoof()
        elif op == '9': crack_hash()
        elif op == '10': geolocalizar()
        elif op == '11': discord_token_grabber()
        elif op == '12': discord_webhook_spam()
        elif op == '13': instagram_scraper()
        elif op == '14': facebook_checker()
        elif op == '15': wifi_stealer()
        elif op == '16': payload_generator()
        elif op == '17': subdomain_scanner()
        elif op == '18': ssh_bruteforce()
        elif op == '19': sqli_scanner()
        elif op == '20': bin_checker()
        elif op == '21':
            clear()
            print(RED + BOLD + "\n[!] Cerrando Payback. Hasta la próxima.\n" + RESET)
            time.sleep(1)
            sys.exit(0)
        else:
            print(RED + "[!] Opción inválida." + RESET)
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(RED + "\n[!] Interrupción detectada. Saliendo..." + RESET)
        sys.exit(0)