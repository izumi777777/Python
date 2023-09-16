from testapp.views import app
from flask.testing import FlaskClient

def test_index():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hi! kikumura!' in response.data