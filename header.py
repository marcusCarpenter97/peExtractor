"""Extracts the PE header from the files."""
import os
import pefile

mal_dir = "../malware"
res_dir = "malware_headers"

with open("pefiles.txt", "r") as txt:
    file_names = txt.readlines()

file_names = [name.strip() for name in file_names]

for name in file_names:
    pepath = os.path.join(mal_dir, name)
    pe = pefile.PE(pepath)
    savpath = os.path.join(res_dir, name)
    with open(savpath, "w") as txt:
        print(pe, file=txt)
