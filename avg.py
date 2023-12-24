import os
import json
import pandas as pd

# Get vs batch
vs_number = input("Enter VS number: ")
vs_dir = f"VirusShare_00{vs_number}"
vs_path = os.path.join("../", vs_dir)
vs_batch_names = pd.DataFrame(os.listdir(vs_path), columns=["sample"])

# Get table with all vt submissions
submitted_files = pd.read_csv("../VirusTotal-PublicUploader/submitted_files.csv")  # Lines are being appended by another script.

# Extract from all vt submissions only the rows in vs batch
submission_table = pd.merge(vs_batch_names, submitted_files, how='inner', on=["sample"])

def get_filenames_for_av(av_name):
    av_timeout = []
    av_malicious = []
    av_unsused = []

    for vs_name, vt_id in submission_table.values:
        analysis_path = os.path.join("../VirusTotal-PublicUploader/analyses", vt_id)
        with open(analysis_path, "r") as analysis:
           analysis_data = json.load(analysis) 
        try:
            if analysis_data["data"]["attributes"]["results"][av_name]["category"] == "malicious":
                av_malicious.append(vs_name)
            if analysis_data["data"]["attributes"]["results"][av_name]["category"] == "timeout":
                av_timeout.append(vs_name)
        except KeyError:
            av_unsused.append(vs_name)

    return av_timeout, av_malicious, av_unsused

extension_path = f"extensions00{vs_number}.csv"

extensions = pd.read_csv(extension_path, names=["name", "extension"])

extensions["name"] = extensions["name"].apply(lambda x: x[20:])

avg_timeout, avg_malicious, avg_unused = get_filenames_for_av("AVG")

avg_t_extensions = pd.merge(pd.DataFrame(avg_timeout, columns=["name"]), extensions, how='inner', on=["name"])
avg_m_extensions = pd.merge(pd.DataFrame(avg_malicious, columns=["name"]), extensions, how='inner', on=["name"])
avg_u_extensions = pd.merge(pd.DataFrame(avg_unused, columns=["name"]), extensions, how='inner', on=["name"])

avg_t_extensions.groupby(["extension"]).count().to_csv(f"{vs_number}avgTimeoutExtensions.csv")
avg_m_extensions.groupby(["extension"]).count().to_csv(f"{vs_number}avgMaliciousExtensions.csv")
avg_u_extensions.groupby(["extension"]).count().to_csv(f"{vs_number}avgUnusedExtensions.csv")
