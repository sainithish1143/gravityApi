import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from fastapi import FastAPI, UploadFile, File, HTTPException


app = FastAPI()

# convert csv to json  
def csv_reader(metadata_file_path):
    with open(metadata_file_path, 'r') as file:
        csv_file = file.readlines()
        return(csv_file)


# paths for metadat and SKU files
metadata_file_path = os.path.abspath("temp/metadata.csv")
sku_file_path = os.path.abspath("temp/sku.csv")

metadata_file = csv_reader(metadata_file_path)
sku_file = csv_reader(sku_file_path)

# storing csv data into list of json
locations = []
departments = []
categories = []
subcategories = []
skus = []

for line in metadata_file[1:]:
    data = line.replace("\n","").split(",")
    counter = metadata_file.index(line)

    locations.append({"location_id":counter, "location":data[0]})
    departments.append({"department_id":counter, "department":data[1], "location_id":counter})
    categories.append({"category_id":counter, "category":data[2], "department_id":counter})
    subcategories.append({"subcategory_id:":counter, "subcategory":data[3] ,"category_id":counter})

for line in sku_file:
    data = line.replace("\n","").split(",")

    skus.append({"SKU":data[0], "name":data[1], "location":data[2], "department":data[3], "category":data[4], "subcategory":data[5]})


class SKU(BaseModel):
    location: str
    department: str
    category: str
    subcategory: str
    
# Api for getting location details
@app.get('/api/v1/location')
def location():
    return locations

@app.get("/api/v1/location/{location_id}/department")
def department(location_id: int):
    result = [dep for dep in departments if dep["location_id"] == location_id]
    if not result:
        raise HTTPException(status_code=404, detail="Departments not found")
    return result

@app.get("/api/v1/location/{location_id}/department/{department_id}/category")
def category(location_id: int, department_id: int):
    deps = [dep for dep in departments if dep["location_id"] == location_id and dep["department_id"] == department_id]
    if not deps:
        raise HTTPException(status_code=404, detail="Department not found in this location")
    
    result = [cat for cat in categories if cat["department_id"] == department_id]
    if not result:
        raise HTTPException(status_code=404, detail="Categories not found")
    return result

@app.get("/api/v1/location/{location_id}/department/{department_id}/category/{category_id}/subcategory")
def subcategory(location_id: int, department_id: int, category_id: int):
    cats = [cat for cat in categories if cat["department_id"] == department_id and cat["category_id"] == category_id]
    if not cats:
        raise HTTPException(status_code=404, detail="Category not found in this department")
    
    result = [subcat for subcat in subcategories if subcat["category_id"] == category_id]
    if not result:
        raise HTTPException(status_code=404, detail="Subcategories not found")
    return result

@app.post("/api/v1/location/{location_id}/department/{department_id}/category/{category_id}/subcategory/{subcategory_id}")
def create_sku(location_id: int, department_id: int, category_id: int, subcategory_id: int, sku: SKU):
    skus.append(sku.dict())
    return sku

@app.post("/api/v1/search_skus")
def search_skus(metadata: SKU):
    for s in skus:
        print(s)
    result = [sku for sku in skus if sku["location"] == metadata.location and 
                                    sku["department"] == metadata.department and 
                                    sku["category"] == metadata.category and 
                                    sku["subcategory"] == metadata.subcategory]
    if not result:
        raise HTTPException(status_code=404, detail="No SKUs found for the given metadata")
    return result
