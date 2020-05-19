import json

with open('/home/airflow/gcs/data/2010.json', 'r') as f:
    json_data = json.load(f)

with open('/home/airflow/gcs/data/2010_jsonl.json', 'w') as outfile:
    for entry in json_data:
        json.dump(entry, outfile)
        outfile.write('\n')