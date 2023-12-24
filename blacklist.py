import os
import json
import pandas as pd

detection_methods = []
vt_dir = "../VirusTotal-PublicUploader/analyses"
for f in os.listdir(vt_dir):
    path = os.path.join(vt_dir, f)
    with open(path, "r") as jf:
        data = json.load(jf)
    for av in data["data"]["attributes"]["results"]:
        detection_methods.append(data["data"]["attributes"]["results"][av]["method"])

dm = pd.DataFrame(detection_methods)
print(dm.groupby([0]).count())
