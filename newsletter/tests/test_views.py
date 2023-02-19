from django.test import Client


def test_main_view():
    client = Client()

    response = client.get('/')

    assert response.status_code == 200

