#common headers
def common_headers_json():
    headers={
        "Content-Type": "application/json",
    }
    return headers
def common_headers_for_put_delete():
    headers={
        "Content-Type": "application/json",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM=",
    }
    return headers
def commom_headers_xml():
    headers={
        "Content-Type": "application/json",
        "Content-Type" : "application/xml"
    }
    return headers