import os
import csv
import magic

directory = input("Enter dir for files: ")

for idx, f in enumerate(os.listdir(directory)):
    path = os.path.join(directory, f)
    print(f"{idx} : {path}")

    extension = magic.from_file(path, mime=True)
    with open("file-extensions.csv", "a", newline="") as csv_file:
        row_writer = csv.writer(csv_file)
        row_writer.writerow([path, extension])

