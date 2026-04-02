import os
import time
from ingestion.ingestion_pipeline import ingest_json

folder = "data/raw"

processed = set()

while True:

    for file in os.listdir(folder):

        if file.endswith(".json") and file not in processed:

            path = os.path.join(folder, file)

            print("New file detected:", file)

            ingest_json(path)

            processed.add(file)

    time.sleep(10)