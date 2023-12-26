#read the file as csv or excel and put that data into our project
#to read file we need to install openpyxl from pip
import requests
import pytest
from src.constants.API_Constants import APIConstants
from src.helpers.utils import common_headers_json
import openpyxl
def read_credentials_from_excel(file_path):
    credentials=[]
    workbook=openpyxl.load_workbook(file_path)
    sheet=workbook.active
    for row in sheet.iter_rows(min_row=2,values_only=True):
        username,password=row
        credentials.append({"username":username,"password":password})
        return credentials
def make_request_auth(username,password):
    payload={
        "username":username,
        "password":password
    }
    response=requests.post(APIConstants.url_create_token(),headers=common_headers_json(),json=payload)
    return response

def test_post_cerate_token():
    #file_path="testdata_ddt.xlsx"
    file_path= "/tests/datadriventesting/testdata_ddt.xlsx"
    credentials=read_credentials_from_excel(file_path)
    for user_cred in credentials:
        username=user_cred["username"]
        password=user_cred["password"]
        print(username,password)
        response=make_request_auth(username,password)
        print(response)
        assert response.status_code==200

