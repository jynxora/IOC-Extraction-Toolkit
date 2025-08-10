import re
from datetime import datetime

filename = input("Enter your FILE name (.log): ")

domainPattern = re.compile(r"https?://([\w\.-]+)", re.IGNORECASE)

with open(filename, "r", errors="ignore") as f:
    text = f.read()

domains = domainPattern.findall(text)
unique_domains = sorted(set(domains))

if domains:
    print(f"\nTotal {len(domains)} domains in {filename} found.")
    print(f"\nTotal Unique {len(unique_domains)} domains in {filename} found:")
    for domain in unique_domains:
        print(" ", domain)
    with open("DomainsFound.txt", "a") as out:
        out.write("\n" + "="*50 + "\n")
        out.write(f"Domain Results from file: {filename}  (Scanned: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')})\n")
        out.write(f"Total {len(domains)} domains found.\n")
        out.write(f"Total Unique domains found - {len(unique_domains)}:\n")
        for domain in unique_domains:
            out.write(domain + "\n")
        out.write("="*50 + "\n\n")

    print("\nDomain results appended to DomainsFound.txt")

else:
    print(f"NO domains found in {filename}.")
