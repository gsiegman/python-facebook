from django.conf.urls.defaults import *


urlpatterns = patterns("facebook.extras.django.facebook.views",
    url(r"^authenticate/$", "authenticate_view", name="facebook_authenticate"),
    url(r"^deauthorize/$", "deauthorize", name="facebook_deauthorize"),
)
