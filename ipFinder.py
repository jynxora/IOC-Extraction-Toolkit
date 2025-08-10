import re
from datetime import datetime

filename = input("Enter your FILE name (.log): ")

ipPattern = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")

with open(filename, "r", errors="ignore") as f:
        text = f.read()

IPs = ipPattern.findall(text)
UniqueIPs = sorted(set(IPs))    # set data-types removes duplicates

if IPs:
        print(f"\nTotal {len(IPs)} IP addresses in {filename} found.")
        print(f"\nTotal Unique {len(IPs)} IP addresses in {filename} found:")
        for ip in UniqueIPs:
                print(" ", ip)

        with open("IPsFound.txt", "a") as out:
                out.write("\n" + "="*50 + "\n")
                out.write(f"Results from file: {filename}(Scanned: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')})\n")
                out.write(f"Total {len(IPs)} IP addresses Found.\n")
                out.write(f"Total Unique IP addresses found - {len(UniqueIPs)}:\n")
                for ip in UniqueIPs:
                        out.write(ip+"\n")
                out.write("="*50 + "\n\n")
        print("\nResults saved to IPsFound.txt")
else:
        print(f"NO IP address found in {filename}.")
