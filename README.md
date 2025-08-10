# IOC Extraction Toolkit

A lightweight Python-based toolkit to extract **Indicators of Compromise (IOCs)** from log files, including:

- **IP Addresses (IPv4)**
- **Domain Names**
- **MD5 & SHA256 Hashes**

Built as part of the #700DaysOfSkill challenge to create practical, field-ready cybersecurity tools.  
Tested on simulated Apache access logs from a compromised server environment.

---

## Features
- Extract and store unique IPs, Domains, and Hashes.
- Append results to respective `.txt` files without overwriting.
- Automatically timestamps every scan.
- Duplicate removal and sorted output for clean analysis.

---

## Scripts
1. **IPFinder.py** – Extracts IPv4 addresses.
2. **DomainFinder.py** – Extracts domain names (malicious & clean).
3. **HashFinder.py** – Extracts MD5 and SHA256 hashes.

Each script:
- Prompts for the file name (must be in the same folder).
- Saves results in a human-readable `.txt` log.
- Uses regex patterns for efficient parsing.

---

## Example Output (IP Extraction)

==================================================

Results from file: access_log_1.log (Scanned: 2025-08-10 17:36:12)
Total 50 IP addresses Found.
Total Unique IP addresses found - 7:
45.77.23.12
66.102.12.54
13.107.21.200
103.45.67.89
8.8.8.8
192.168.56.23
142.250.182.4

==================================================

---

## Detection Methodology

| IOC Type  | Regex Pattern | Notes |
|-----------|--------------|-------|
| IPv4      | `\b(?:\d{1,3}\.){3}\d{1,3}\b` | Matches dotted IPv4 addresses |
| Domain    | `https?://([\w\.-]+)` | Matches clean & malicious domains |
| MD5       | `\b[a-fA-F0-9]{32}\b` | Detects MD5 hashes |
| SHA256    | `\b[a-fA-F0-9]{64}\b` | Detects SHA256 hashes |

---

## READ the Report/Scripts:

[Report (PDF Format)](./IOCExtractionReport.pdf)

[Report (Markdown Format)](./IOCExtractionReport.md)

[IP Finder](./ipFinder.py)

[Domain Finder](./domainFinder.py)

[Hashed Text Finder](./hashesFinder.py)

---
