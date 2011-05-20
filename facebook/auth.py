import base64
import hashlib
import hmac
import json
import requests


def app_authentication(auth_code, app_id, app_secret, redirect_uri):
    """
    Returns an access token
    """
    response = requests.get("https://graph.facebook.com/oauth/access_token", {
        "client_id": app_id,
        "client_secret": app_secret,
        "code": auth_code,
        "redirect_uri": redirect_uri
    })
    
    return response.content["access_token"][-1]


def parse_signed_request(signed_request, app_secret):
    # translated to Python from PHP example at:
    # http://developers.facebook.com/docs/authentication/signed_request/
    split_request = signed_request.split(".", 2)
    
    encoded_sig = str(split_request[0])
    payload = str(split_request[1])
    
    # decode
    decoded_sig = base64.urlsafe_b64decode(encoded_sig + "==")
    data = json.loads(base64.urlsafe_b64decode(payload + "=="))
    
    # verify signature
    if data["algorithm"] != "HMAC-SHA256":
        raise ValueError("Unknown algorithm. Expected HMAC-SHA256")
    else:
        expected_sig = hmac.new(
            app_secret, 
            msg=payload, 
            digestmod=hashlib.sha256
        ).digest()
    
    if decoded_sig != expected_sig:
        raise ValueError("Unexpected signature received.")
    
    return data
