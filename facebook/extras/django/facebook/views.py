import urllib

from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import login, authenticate

from facebook.auth import parse_signed_request
from facebook.extras.django.facebook.models import FacebookProfile


def authenticate_view(request):
    code = request.GET.get("code", "")
    app_url = settings.FACEBOOK_APP_SETTINGS["APP_URL"]
    
    if code:
        user = authenticate(token=code, request=request)
        
        if user:
            login(request, user)
            return HttpResponseRedirect(app_url)
        else:
            return HttpResponseForbidden()
    else:
        args = {
            "redirect_uri": settings.FACEBOOK_APP_SETTINGS["AUTH_URL"],
            "client_id": settings.FACEBOOK_APP_SETTINGS["APP_ID"],
            "scope": ",".join(settings.FACEBOOK_APP_SETTINGS["PERMISSIONS"])
        }
        
        return HttpResponse('<html><body><script type="text/javascript">top.location.href="https://graph.facebook.com/oauth/authorize?' + urllib.urlencode(args) + '"</script></body</html>')


@csrf_exempt
def deauthorize(request):
  if "signed_request" in request.POST:
    sr = parse_signed_request(request.POST["signed_request"], settings.FACEBOOK_APP_SETTINGS["APP_SECRET"])
    try:
      profile = FacebookProfile.objects.get(facebook_id=sr["user_id"])
      profile.user.delete()
    except:
      pass
  return HttpResponse()
