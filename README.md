### Steps to be performed
- Pull this repo in your workspace
    - Open your terminal or command prompt.
    - cd /path/to/your/workspace
    - Run the git clone command `git clone https://github.com/sainithish1143/test.git`.

- run `setup.sh` to install dependencies and starting the server

- Navigate to swagger using localhost address with mentioned port (eg. [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) or use below API endpoints.

## API Endpoints ##
>**GET** `/api/v1/location` : Returns all locations.
>
>**GET** `/api/v1/location/{location_id}/department` : Returns departments for a given location.
>
>**GET** `/api/v1/location/{location_id}/department/{department_id}/category` : Returns categories for a given department.
>
>**GET** `/api/v1/location/{location_id}/department/{department_id}/category/{category_id}/subcategory` : Returns subcategories for a given category.
>
>**POST** `/api/v1/location/{location_id}/department/{department_id}/category/{category_id}/subcategory/{subcategory_id}` : Creates a new SKU for the given metadata.
>
>**POST** `/api/v1/search_skus` : Takes metadata as input and returns matching SKUs.

  
