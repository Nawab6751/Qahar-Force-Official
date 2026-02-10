import os, sys, time, sqlite3, requests

# Database Setup
db = sqlite3.connect("qahar_data.db")
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS targets (id INTEGER PRIMARY KEY, ip TEXT, info TEXT)")
db.commit()

def banner():
    os.system('clear')
    print("\033[1;31m============================================")
    print("\033[1;37m      Q A H A R    F O R C E    V7.0")
    print("\033[1;31m============================================")
    print("\033[1;33m  Commander: NAWAB ZADA | Team: QAHAR")
    print("\033[1;31m============================================\033[0m")

def wa_unban():
    banner()
    num = input("\033[1;37mBan Number (with code): \033[0m")
    print(f"\n\033[1;32m[!] Support Mail Drafted for {num}:")
    print("\033[1;33mSubject: Account Deactivation Appeal")
    print(f"Message: My number {num} is banned by mistake. Please restore it.\033[0m")
    input("\nPress Enter to return...")

def main():
    while True:
        banner()
        print("\033[1;32m[1]\033[1;37m WhatsApp Unban Appeal")
        print("\033[1;32m[2]\033[1;37m IP Tracker (With Database)")
        print("\033[1;32m[3]\033[1;37m View Saved History")
        print("\033[1;31m[0]\033[1;37m Exit")
        
        opt = input("\n\033[1;31mQahar-Force > \033[0m")
        
        if opt == '1': wa_unban()
        elif opt == '0': sys.exit()
        else: print("Invalid Option!"); time.sleep(1)

if __name__ == "__main__":
    main()
