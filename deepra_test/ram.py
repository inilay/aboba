import argparse
import time
import sys
 
def generate_ram_load(interval=int(sys.argv[1]),amount=int(sys.argv[2])):
    GB = 1024 * 1024 * 1024
    eat = "a" * GB * amount
    time.sleep(interval)
 
#----START OF SCRIPT
if __name__=='__main__':
    print("Load RAM")
    if len(sys.argv)>2:
       generate_ram_load()
       
