"""Checks for the existance of a PE header and creates a list of PE files."""
import os
import pefile

malware = os.listdir("../malware")
size = len(malware)

pefiles = []
for idx, sample in enumerate(malware):
    print(f"{idx}/{size}")
    path = os.path.join("../malware", sample)
    try:
        pe = pefile.PE(path)
    except pefile.PEFormatError:
        continue
    pefiles.append(f"{sample}\n")

print(f"Number of pe files found: {len(pefiles)}")
with open("pefiles.txt", "a") as txt:
    txt.writelines(pefiles)
