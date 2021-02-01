# planet
Get a list of planets from a [public API](http://swapi.dev/api/), saves it on a SQLite database and show the data in a Datatable. Made with Flask.
It's also available an API Rest with the endpoint:
/api/planets/ - lists all the planets

## Images
![](static/img/tela1.png)
![](static/img/tela2.png)
![](static/img/tela3.png)

## Installation
1. Clone the [repo](https://github.com/iasmini/planet):
```shell
    git clone https://github.com/iasmini/planet
```
2. Access the root directory (planet) and run the command:
> **_NOTE:_**  It's recommended doing it within a virtual environment.
```shell
    pip install -r app/requirements.txt
```
3. External packages:  
[Flask~=1.1.2](https://flask.palletsprojects.com/en/1.1.x/)  
[Flask-RESTful==0.3.8](https://flask-restful.readthedocs.io/en/latest/)  
[Flask-SQLAlchemy~=2.4.4](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
[pytest~=6.2.2](https://docs.pytest.org/en/latest/)   
[requests~=2.25.1](https://requests.readthedocs.io/en/master/)  
[SQLAlchemy-serializer~=1.3.4.4](https://github.com/n0nSmoker/SQLAlchemy-serializer)


## How to use it
1. Access the root directory (planet) and run the command:
```shell
    python run.py
```
2. It will be available on: http://127.0.0.1:5000/

## API
### Search by part of the name and climate
```http request
GET "/api/planets/?climate=arid&name=tatooi"
```
Response
```json
{
    "status_code": 200,
    "response": [
        {
            "diameter": "10465",
            "surface_water": "1",
            "name": "Tatooine",
            "id": 1,
            "climate": "arid",
            "gravity": "1 standard",
            "terrain": "desert",
            "orbital_period": "304",
            "rotation_period": "23",
            "population": 200000
        }
    ]
}
```
### Order by any field
```http request
GET "/api/planets/?sort=id" 
```
or
```http request
GET "/api/planets/?sort=id asc"
```
Response
```json
{
    "status_code": 200,
    "response": [
        {
            "diameter": "10465",
            "surface_water": "1",
            "name": "Tatooine",
            "id": 1,
            "climate": "arid",
            "gravity": "1 standard",
            "terrain": "desert",
            "orbital_period": "304",
            "rotation_period": "23",
            "population": 200000
        },
        {
        "other planets": "(...)"
        },
        {
            "diameter": "unknown",
            "surface_water": "unknown",
            "name": "Umbara",
            "id": 60,
            "climate": "unknown",
            "gravity": "unknown",
            "terrain": "unknown",
            "orbital_period": "unknown",
            "rotation_period": "unknown",
            "population": null
        }
    ]
}
```
### Order by any field (desc)
```http request
GET "/api/planets/?sort=name desc"
```
Response
```json
{
    "status_code": 200,
    "response": [
        {
            "diameter": "0",
            "surface_water": "unknown",
            "name": "unknown",
            "id": 28,
            "climate": "unknown",
            "gravity": "unknown",
            "terrain": "unknown",
            "orbital_period": "0",
            "rotation_period": "0",
            "population": null
        },
        {
        "other planets": "(...)"
        },
        {
            "diameter": "12500",
            "surface_water": "40",
            "name": "Alderaan",
            "id": 2,
            "climate": "temperate",
            "gravity": "1 standard",
            "terrain": "grasslands, mountains",
            "orbital_period": "364",
            "rotation_period": "24",
            "population": 2000000000
        }
    ]
}
```
### Get paginated results
```http request
GET "/api/planets/?climate=temperate&page=2"
```
Response
```json
{
    "status_code": 200,
    "response": {
        "page": 2,
        "items_per_page": 10,
        "count": 23,
        "previous": "/planets?page=1",
        "next": "",
        "results": [
            {
                "diameter": "6400",
                "surface_water": "98",
                "name": "Bestine IV",
                "id": 26,
                "climate": "temperate",
                "gravity": "unknown",
                "terrain": "rocky islands, oceans",
                "orbital_period": "680",
                "rotation_period": "26",
                "population": 62000000
            },
            {
                "diameter": "14050",
                "surface_water": "10",
                "name": "Ord Mantell",
                "id": 27,
                "climate": "temperate",
                "gravity": "1 standard",
                "terrain": "plains, seas, mesas",
                "orbital_period": "334",
                "rotation_period": "26",
                "population": 4000000000
            },
            {
                "diameter": "11030",
                "surface_water": "100",
                "name": "Mon Cala",
                "id": 31,
                "climate": "temperate",
                "gravity": "1",
                "terrain": "oceans, reefs, islands",
                "orbital_period": "398",
                "rotation_period": "21",
                "population": 27000000000
            },
            {
                "diameter": "13500",
                "surface_water": "40",
                "name": "Chandrila",
                "id": 32,
                "climate": "temperate",
                "gravity": "1",
                "terrain": "plains, forests",
                "orbital_period": "368",
                "rotation_period": "20",
                "population": 1200000000
            },
            {
                "diameter": "7900",
                "surface_water": "unknown",
                "name": "Toydaria",
                "id": 34,
                "climate": "temperate",
                "gravity": "1",
                "terrain": "swamps, lakes",
                "orbital_period": "184",
                "rotation_period": "21",
                "population": 11000000
            },
            {
                "diameter": "10480",
                "surface_water": "unknown",
                "name": "Dathomir",
                "id": 36,
                "climate": "temperate",
                "gravity": "0.9",
                "terrain": "forests, deserts, savannas",
                "orbital_period": "491",
                "rotation_period": "24",
                "population": 5200
            },
            {
                "diameter": "10120",
                "surface_water": "unknown",
                "name": "Haruun Kal",
                "id": 42,
                "climate": "temperate",
                "gravity": "0.98",
                "terrain": "toxic cloudsea, plateaus, volcanoes",
                "orbital_period": "383",
                "rotation_period": "25",
                "population": 705300
            },
            {
                "diameter": "unknown",
                "surface_water": "20",
                "name": "Cerea",
                "id": 43,
                "climate": "temperate",
                "gravity": "1",
                "terrain": "verdant",
                "orbital_period": "386",
                "rotation_period": "27",
                "population": 450000000
            },
            {
                "diameter": "13400",
                "surface_water": "unknown",
                "name": "Dorin",
                "id": 49,
                "climate": "temperate",
                "gravity": "1",
                "terrain": "unknown",
                "orbital_period": "409",
                "rotation_period": "22",
                "population": null
            },
            {
                "diameter": "unknown",
                "surface_water": "unknown",
                "name": "Champala",
                "id": 50,
                "climate": "temperate",
                "gravity": "1",
                "terrain": "oceans, rainforests, plateaus",
                "orbital_period": "318",
                "rotation_period": "27",
                "population": 3500000000
            }
        ]
    }
}
```
### Combine searching, ordering and pagination
```http request
GET "/api/planets/?climate=arid&name=tatooi&page=1&sort=name asc"
```
Response
```json
{
    "status_code": 200,
    "response": {
        "page": 1,
        "items_per_page": 10,
        "count": 1,
        "previous": "",
        "next": "",
        "results": [
            {
                "diameter": "10465",
                "surface_water": "1",
                "name": "Tatooine",
                "id": 1,
                "climate": "arid",
                "gravity": "1 standard",
                "terrain": "desert",
                "orbital_period": "304",
                "rotation_period": "23",
                "population": 200000
            }
        ]
    }
}
```
### Response errors
| Status code      | Response                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------- |
|       200        | Success                                                                                     |
|       400        | Não foram encontrados planetas de acordo com os parâmetros informados.                      |
|       400        | Página {page} não existe. Página mínima 1.                                                  |
|       400        | Página {page} não existe. Página máxima de acordo com os parâmetros informados: {max_page}. |

## Running tests
> **_NOTE:_**  It's recommended doing it within a virtual environment.
1. Access the root directory (planet) and run the command
```shell
    pytest
```
All the tests must pass:
![](static/img/pytest.png)

## Building the package
To run tests you must build the package if there isn't one. Access the root directory (planet) and run the command:
> **_NOTE:_**  It's recommended doing it within a virtual environment.
```shell
    pip install -e .
```
