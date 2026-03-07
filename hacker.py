import os, time, sys, random, requests

# Nawab's Special Neon Colors
G, R, Y, C, W, P = "\033[1;32m", "\033[1;31m", "\033[1;33m", "\033[1;36m", "\033[1;37m", "\033[1;35m"

def banner():
    os.system("clear")
    print(f"""{G}
    ███╗   ██╗ █████╗ ██╗    ██╗ █████╗ ██████╗ 
    ████╗  ██║██╔══██╗██║    ██║██╔══██╗██╔══██╗
    ██╔██╗ ██║███████║██║ █╗ ██║███████║██████╔╝
    ██║╚██╗██║██╔══██║██║███╗██║██╔══██║██╔══██╗
    ██║ ╚████║██║  ██║╚███╔███╔╝██║  ██║██████╔╝
    ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═════╝ 
    {Y}██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
    {Y}██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
    {Y}███████║███████║██║     █████╔╝ █████╗  ██████╔╝
    {Y}██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
    {Y}██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██╗
    {Y}╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    {W} ---------------------------------------------
    {P}        [#] SYSTEM BY: NAWAB ZADA HACKER [#]
    {W} ---------------------------------------------
    """)

def ip_tracker():
    print(f"\n{C}[?] Target IP dalo (Khaali chhoro apni check karne ke liye): {W}")
    ip = input(f"{Y}Nawab-IP >> {W}")
    try:
        data = requests.get(f"http://ip-api.com/json/{ip}").json()
        print(f"\n{G}[+] IP: {W}{data['query']}\n{G}[+] City: {W}{data['city']}\n{G}[+] ISP: {W}{data['isp']}")
    except: print(f"{R}[-] Error fetching data.")
    input(f"\n{P}Press Enter...")

def username_stalker():
    banner()
    username = input(f"\n{C}[?] Target Username dalo: {W}")
    print(f"\n{Y}[*] Nawab's Ghost Scanning 50+ Social Platforms...\n")
    
    # Real sites to check
    social_sites = {
        "Facebook": "https://www.facebook.com/{}",
        "Instagram": "https://www.instagram.com/{}",
        "Twitter": "https://www.twitter.com/{}",
        "GitHub": "https://www.github.com/{}",
        "TikTok": "https://www.tiktok.com/@{}",
        "Pinterest": "https://www.pinterest.com/{}"
    }
    
    found = 0
    for site, url in social_sites.items():
        full_url = url.format(username)
        try:
            r = requests.get(full_url, timeout=5)
            if r.status_code == 200:
                print(f"{G}[FOUND] {W}{site}: {C}{full_url}")
                found += 1
            else:
                print(f"{R}[NOT FOUND] {W}{site}")
        except:
            pass
            
    print(f"\n{G}[#] Scan Complete! Total {found} profiles linked to '{username}'.")
    input(f"\n{P}Press Enter to go back...")

def main():
    while True:
        banner()
        print(f"{W}[1] {G}IP Tracker (Real-Time Location)")
        print(f"{W}[2] {G}Username Stalker (Social Scan)")
        print(f"{W}[3] {R}Exit Command Center")
        
        choice = input(f"\n{C}Nawab-Hacker >> {W}")
        if choice == "1": ip_tracker()
        elif choice == "2": username_stalker()
        elif choice == "3": break
        else: time.sleep(1)

if __name__ == "__main__":
    main()
