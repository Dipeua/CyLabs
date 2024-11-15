#!/bin/bash

install(){
    echo "[*] Installing requirements to virtual environment"
    pip install -r ../requirements.txt
    echo "[+] Successfully installed all requirements!"

    echo "[*] Starting Django server..."
    if [[ "$OSTYPE" == "msys" ]]; then
        python ../manage.py migrate
        python ../manage.py runserver 0.0.0.0:8000 --insecure
    elif [[ "$OSTYPE" == "linux-gnu" ]]; then
        python ../manage.py migrate
        python3 ../manage.py runserver 0.0.0.0:8000 --insecure
    else
        echo "[-] Unable to start server, system not recognized"
    fi
}

banner(){
    echo "
    +--------------------------------------------------+
    |             CyLabs - The Audit Security Platform |
    |                     By: @Ber1y (Dipeua Berthold) |
    +--------------------------------------------------+
    "
    echo "[*] Initializing virtual environment"
}

detect_windows() {
    if command -v reg.exe > /dev/null && reg.exe query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion" > /dev/null 2>&1; then
        echo "[+] System detected: Windows"
        banner
        
        python -m venv ../.env
        echo "[*] Activating virtual environment"
        . ../.env/Scripts/activate
        
        install
    fi
}

detect_linux() {
    if [ -f "/proc/version" ]; then
        echo "[+] System detected: Linux"
        banner

        python3 -m venv .env
        echo "[*] Activating virtual environment"
        source ../.env/bin/activate
        
        install
    fi
}

# Check the system depending on the platform
echo "[!] Checking the system platform..."
if [[ "$OSTYPE" == "msys" ]]; then
    detect_windows
elif [[ "$OSTYPE" == "linux-gnu" ]]; then
    detect_linux
else
    echo "[-] System not recognized"
fi
