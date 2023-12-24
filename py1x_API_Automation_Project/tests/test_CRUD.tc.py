from src.constants.API_Constants import Base_Url,APIConstants,base_url
import requests
def test_CRUD():
    print(Base_Url)
    url_direc_func=base_url()
    print(url_direc_func)
    requests.get()
    url_class=APIConstants.base_url()
    print(url_class)
