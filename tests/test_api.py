from app import app


def test_search_by_name():
    response = app.test_client().get('/api/planets/?name=Tatooine')

    assert response.json['status_code'] == 200


def test_search_by_partial_name():
    response = app.test_client().get('/api/planets/?name=atooin')

    assert response.json['status_code'] == 200


def test_search_by_climate():
    response = app.test_client().get('/api/planets/?climate=temperate')

    assert response.json['status_code'] == 200


def test_sort_by_id():
    response = app.test_client().get('/api/planets/?sort=climate')

    assert response.json['status_code'] == 200


def test_sort_by_name_desc():
    response = app.test_client().get('/api/planets/?sort=name desc')

    assert response.json['status_code'] == 200


def test_get_page_2():
    response = app.test_client().get('/api/planets/?page=2')

    assert response.json['status_code'] == 200


def test_combined():
    response = app.test_client().get('/api/planets/?climate=arid&name=tatooi&page=1&sort=name asc')

    assert response.json['status_code'] == 200


def test_get_unknown_planet():
    response = app.test_client().get('/api/planets/?name=planet-x&page=1')

    assert response.json['status_code'] == 400


def test_get_min_page():
    response = app.test_client().get('/api/planets/?name=planet-x&page=-1')

    assert response.json['status_code'] == 400


def test_get_max_page():
    response = app.test_client().get('/api/planets/?name=planet-x&page=100')

    assert response.json['status_code'] == 400
