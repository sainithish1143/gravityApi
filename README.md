### Problem tatement ###
[GRAVITY_CODE_TEST.DOCX](https://github.com/sainithish1143/gravityApi/blob/master/Gravity%20CODE%20TEST%20-%20PYTHON.docx)

### Steps to be performed
- Pull this repo in your workspace
    - Open your terminal or command prompt.
    - cd /path/to/your/workspace
    - Run the git clone command `git clone https://github.com/sainithish1143/test.git`.

- run `setup.sh` to install dependencies and starting the server

- Navigate to swagger using localhost address with mentioned port (eg. [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) or use below API endpoints.

## API Endpoints ##
| # |Operation                                                                                                                 |Endpoint                                           |Desription                                          |
|---|:------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------:|:--------------------------------------------------:|
|1  |                                                         **GET**                                                          |                 `/api/v1/location`                |               Returns all locations.               |
|2  |                                                         **GET**                                                          |    `/api/v1/location/{location_id}/department`    |      Returns departments for a given location.     |
|3  |                                                         **GET**                                                          | `/api/v1/location/{location_id}/department/{depart|      Returns categories for a given department.    |
|4  |                                                         **GET**                                                          | `/api/v1/location/{location_id}/department/{depart|   `  Returns subcategories for a given category.   |
|5  |                                                         **POST**                                                         | `/api/v1/location/{location_id}/department/{depart|      Creates a new SKU for the given metadata.     |
|6  |                                                         **POST**                                                         |               `/api/v1/search_skus`               |  Takes metadata as input and returns matching SKUs.|



  
