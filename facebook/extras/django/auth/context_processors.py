from django.conf import settings


def app_settings(request):
    """
    Provides access to the Facebook settings
    """
    facebook = settings.FACEBOOK_APP_SETTINGS
    
    return {"facebook": facebook}
