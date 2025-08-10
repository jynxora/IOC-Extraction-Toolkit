import re
from datetime import datetime

filename = input("Enter your FILE name (.log): ")

md5Pattern = re.compile(r"\b[a-fA-F0-9]{32}\b")
sha256Pattern = re.compile(r"\b[a-fA-F0-9]{64}\b")

with open(filename, "r", errors="ignore") as f:
    text = f.read()

md5Hashes = md5Pattern.findall(text)
sha256Hashes = sha256Pattern.findall(text)

if md5Hashes or sha256Hashes:
    print(f"\nTotal MD5 hashes found: {len(md5Hashes)}")
    print(f"Total Unique MD5: {len(set(md5Hashes))}")
    for h in set(md5Hashes):
        print(" ", h)

    print(f"\nTotal SHA256 hashes found: {len(sha256Hashes)}")
    print(f"Total Unique SHA256: {len(set(sha256Hashes))}")
    for h in set(sha256Hashes):
        print(" ", h)

    with open("HashesFound.txt", "a") as out:
        out.write("\n" + "="*50 + "\n")
        out.write(f"Hash Results from file: {filename}  (Scanned: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')})\n")
        out.write(f"Total MD5 hashes: {len(md5Hashes)}\n")
        out.write(f"Total Unique MD5: {len(set(md5Hashes))}\n")
        for h in sorted(set(md5Hashes)):
            out.write(h + "\n")
        out.write(f"\nTotal SHA256 hashes: {len(sha256Hashes)}\n")
        out.write(f"Total Unique SHA256: {len(set(sha256Hashes))}\n")
        for h in sorted(set(sha256Hashes)):
            out.write(h + "\n")
        out.write("="*50 + "\n")

    print("\nResults saved to HashesFound.txt")
else:
    print(f"No MD5 or SHA256 hashes found in {filename}.")
