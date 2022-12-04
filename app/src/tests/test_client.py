import pytest
from flaskr.main import app

def test_example_route():
    response = app.test_client().get('/example')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == '<p>Hello, World!</p>'

def test_default_get():
    response = app.test_client().get('/')

    expected = "<h1>Hello, 🐍 !</h1>"

    assert response.status_code == 200
    assert expected in response.data.decode('utf-8') 


@pytest.mark.parametrize("name_param", ['alex','josefa','paco'])
def test_different_names_get(name_param):
    response = app.test_client().get(f'/{name_param}')

    expected = f"<h1>Hello {name_param} !</h1>"

    assert response.status_code == 200
    assert expected in response.data.decode('utf-8') 