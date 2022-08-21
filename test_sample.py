import pytest
import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_index_route():
    data1={
    "internalId": "3",
    "name": "Harry",
    "last_name": "Potter",
    "phone": "(702) 315-7822 x250"
    }
    response = client.post('infoUsers', data=json.dumps(data1), headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    assert response.json() == { "message": "USER_CREATED"}


    data2={
    "internalId": "3",
    "name": "Harry",
    "last_name": "Potter",
    "phone": "(702) 315-7822 x250",
    "idUsuario": "3"
    }
    response = client.get('infoUsers/3')
    assert response.status_code == 200
    assert response.json() == data2


    data2={
    "name": "SAM",
    "last_name": "Potter",
    }
    response = client.put('infoUsers/3', data=json.dumps(data2), headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    assert response.json() == { "message": "USER_UPDATED"}


    response = client.delete('infoUsers/3')
    assert response.status_code == 200
    assert response.json() == { "message": "USER_DELETED"}