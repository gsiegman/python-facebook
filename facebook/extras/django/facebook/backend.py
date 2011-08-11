import time

from django.conf import settings

from django.contrib.auth.models import User

from facebook.auth import app_authentication
from facebook.extras.django.facebook.models import FacebookProfile
from facebook.graph import Graph


class FacebookAuthBackend(object):
    supports_anonymous_user = False
    
    def authenticate(self, token=None, request=None):
        access_token = app_authentication(
            token,
            settings.FACEBOOK_APP_SETTINGS["APP_ID"],
            settings.FACEBOOK_APP_SETTINGS["APP_SECRET"],
            settings.FACEBOOK_APP_SETTINGS["AUTH_URL"]
        )
        
        profile = Graph(access_token).get_user()
        
        try:
            fb_profile = FacebookProfile.objects.get(
                facebook_id=str(profile["id"])
            )
            fb_profile.access_token = access_token
            fb_profile.save()
            user = fb_profile.user
        except FacebookProfile.DoesNotExist:
            user = User.objects.create(
                username=profile["id"],
                email=profile["email"],
                first_name=profile["first_name"],
                last_name=profile["last_name"]
            )
            
            formatted_dob = time.strftime(
                "%Y-%m-%d", 
                time.strptime(profile["birthday"], "%m/%d/%Y")
            )
            
            fb_profile = FacebookProfile.objects.create(
                user=user,
                facebook_id=profile["id"],
                access_token=access_token,
                dob=formatted_dob
            )
        
        return user
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
    
