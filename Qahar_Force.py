import os, sys

# Author Identity
__author__ = "Nawab6751"

def security_check():
    if __author__ != "Nawab6751":
        print("\033[1;31m❌ ERROR: Unauthorized modification detected!")
        print("\033[1;33m💡 Ye tool Nawab Zada ki malkiyat hai. Naam badalne ki koshish na karein!\033[0m")
        sys.exit()

security_check()

