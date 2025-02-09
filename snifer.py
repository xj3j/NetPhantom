# What we do here is import scapy and then we import a function called sniff,
# which allows us to capture packets on the network.
from scapy.all import sniff

red_text = "\033[91m" + r"""
███╗   ██╗███████╗████████╗██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔═══██╗████╗ ████║
██╔██╗ ██║█████╗     ██║   ██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
██║╚██╗██║██╔══╝     ██║   ██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
██║ ╚████║███████╗   ██║   ██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
""" + "\033[0m"

def packets(packet):
    if packet.haslayer("IP"):  
        print(f"Paquete capturado: {packet['IP'].src} ➡️ {packet['IP'].dst}")  


# Menú de opciones
def main():
    while True:
        print(red_text)
        print("\n📡 NetPhantom - Packet Sniffer 👻")
        print("1️⃣  Start sniffing")
        print("2️⃣  Working on it")
        print("3️⃣  exit")
        
        choice = input("select an option: ")
        
        if choice == "1":
            print("Sniffer sniffing🚬🚬")
            print("If u wanna cancel press ctrl+C")
            sniff(prn=packets, store=False)
        elif choice == "2":
            print("\n[!] Working on it")
        elif choice == "3":
            print("\n[+] Leaving ")
            break
        else:
            print("\n[!] Error")


if __name__ == "__main__":
    main()



