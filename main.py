import csv
import json
import os
from fastapi import FastAPI
app = FastAPI()

# convert csv to json
def csv_to_json(metadata_file_path):
    with open(metadata_file_path, 'r') as file:
        print(file.readline())
        csv_file = csv.DictReader(file)
        return(list(csv_file))


# paths for metadat and SKU files
metadata_file_path = os.path.abspath("temp/metadata.csv")
sku_file_path = os.path.abspath("temp/sku.csv")

metadata_json = csv_to_json(metadata_file_path)
sku_json = csv_to_json(sku_file_path)

# sample
@app.get('/api/v1/location')
def location():
    return metadata_json[1]






