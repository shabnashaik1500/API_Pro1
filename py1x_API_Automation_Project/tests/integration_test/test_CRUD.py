from src.helpers.api_requests_wrapper import post_requests,put_requests,delete_requests
from src.constants.API_Constants import APIConstants
from src.helpers.utils import common_headers_json,common_headers_for_put_delete
from src.helpers.payload_manager import payload_create_booking,payload_create_token
from src.helpers.common_verification import verify_response_key_should_not_be_none,verify_http_status_code


import requests
import pytest

class TestCreateBooking(object):
    @pytest.fixture()
    def create_token(self):
        response=post_requests(url=APIConstants.url_create_token(),
                               headers=common_headers_json(),auth=None,
                               payload=payload_create_token(),in_json=False)
        verify_http_status_code(response,200)
        token=response.json()["token"]
        verify_response_key_should_not_be_none(token)
        print(token)
        return token
    @pytest.fixture()
    def create_booking(self):
        response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                 payload=payload_create_booking(), in_json=False)
        print(response)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, 200)
        bookingid = response.json()["bookingid"]
        return bookingid
    def test_put_booking(self,create_booking,create_token):#token and booking id from create booking
        bookingId=create_booking
        put_url=APIConstants.url_create_booking() + "/" +str(bookingId)
        response=put_requests(url=put_url,headers=common_headers_for_put_delete(),auth=None,payload=payload_create_booking(),in_json=False)
        print((response.json()))
        print(create_booking)
        #print(create_token)
    #def test_delete_booking(self,create_booking,create_token):
     #   bookingId = create_booking
      #  delete_url = APIConstants.url_create_booking() + "/" + str(bookingId)
       # response = delete_requests(url=delete_url, headers=common_headers_for_put_delete(), auth=None,
        #                      payload=None, in_json=False)
