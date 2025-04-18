# imports
import time, sys, os, datetime, socket

def scan():
    os.system("clear")
    print("\n\n*** Python TCP Port Scanner ***\n\n")

    host = input("Enter the Host IP address: ")
    sport = int(input("Enter starting Port #: "))
    eport = int(input("Enter ending Port #: "))

    st = datetime.datetime.now().strftime("%a %b %d %Y, %I:%M:%S %p")
    print(f"\nStarted port scan on {host} at {st}...")

    for port in range(sport, eport + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)

        result = sock.connect_ex((host, port))

        if result == 0:
            print(f"Port {port} is open")

        sock.close

    ft = datetime.datetime.now().strftime("%a %b %d %Y, %I:%M:%S %p")
    print(f"\nPort scan completed at {ft}.")

# loop controls program flow
answer = "yes"
while answer == "yes":
    scan()
    time.sleep(3)
    answer = input("\nScan another host? Type yes to proceed or any other key(s) to quit: ")

sys.exit()