import requests
from fastapi import Response, status, APIRouter
from pydantic import BaseModel
from typing import Union

prefix = "infoUsers"
router = APIRouter(prefix="/"+prefix,)
url = 'https://62fd7b30b9e38585cd52637e.mockapi.io/udem/taller2/'

class IData(BaseModel):
    name: Union[str, None] = None
    last_name: Union[str, None] = None
    phone: Union[str, None] = None

class IDataCreate(IData):
    internalId: Union[str, None] = None

def checkIsEmpty(data):
    valueData = list(data.values()) #list of values 
    existData = any(elem is not None for elem in valueData) #exist info in info send by user
    if not existData:
        return True

@router.get("/{idUsuario}", status_code=200)
def get_info_users(idUsuario: str, response: Response):
    try:
        consult = requests.get(url + prefix + '/?idUsuario=' + idUsuario, timeout=5)
        data = consult.json()
        if len(data) == 1:
            response = data[0]
            return response
        response.status_code = status.HTTP_204_NO_CONTENT
    except:
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "message": "ERROR_FINDING_USER"}

@router.post("", status_code=200)
def create_info_users(infoUser: IDataCreate, response: Response):
    data = infoUser.dict()
    isEmpty = checkIsEmpty(data)
    if (isEmpty):
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "message": "NOT_DATA_CREATE"}
    try:
        response = requests.post(url + prefix, data, timeout=5)
        if response.status_code == 201:
            return { "message": "USER_CREATED"}
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "message": "ERROR_CREATING_USER"}
    except:
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "message": "ERROR_CREATING_USER"}

@router.delete("/{idUsuario}", status_code=200)
def delete_info_users(idUsuario: str, response: Response):
    try:
        consult = requests.delete(url + prefix + '/' + idUsuario)
        data = consult.json()
        if type(data) is dict: 
            return { "message": "USER_DELETED"}
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "message": "USER_NOT_FOUND"}
    except:
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "message": "ERROR_FINDING_USER"}

@router.put("/{idUsuario}", status_code=200)
def update_info_users(idUsuario: str, infoUser: IData, response: Response):
    data = infoUser.dict() #data in json format
    isEmpty = checkIsEmpty(data)
    if (isEmpty):
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "message": "NOT_DATA_UPDATE"}
    try:
        consult = requests.put(url + prefix + '/' + idUsuario, data)
        if consult.status_code == 200:
            return { "message": "USER_UPDATED"}
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "message": "USER_NOT_EXIST"}
    except:
        response.status_code = status.HTTP_404_NOT_FOUND
        return { "message": "ERROR_UPDATING_USER"}


