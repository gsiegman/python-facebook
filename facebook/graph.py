import json
import requests


# Official Graph API documentation can be found http://developers.facebook.com/docs/reference/api/

class Graph(object):
    
    def __init__(self, access_token="", endpoint_root="https://graph.facebook.com"):
        self.access_token = access_token
        self.endpoint_root = endpoint_root
    
    def _request(self, path, method, data={}):
        assert method in ("GET", "POST", "DELETE")
        
        if self.access_token:
            data["access_token"] = self.access_token
        
        response = getattr(requests, method.lower())("%s/%s" % (self.endpoint_root, path), data)
        content = json.loads(response.content)
        
        return content
    
    def get_user(self, facebook_id="me"):
        return self._request(facebook_id, "GET")
    
    def get_user_friends(self, facebook_id="me"):
        return self._request("/".join([facebook_id, "friends"]), "GET")
    
    def get_user_picture(self, facebook_id="me"):
        return "/".join([self.endpoint_root, facebook_id, "picture"])
    
    def get_user_likes(self, facebook_id="me"):
        return self._request("/".join([facebook_id, "likes"]), "GET")
