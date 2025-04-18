# imports
import time, sys

def scan():
    

# loop controls program flow
answer = "yes"
while answer == "yes":
    scan()
    time.sleep(3)
    answer = input("\nScan another host? Type yes to proceed or any other key(s) to quit: ")

sys.exit()