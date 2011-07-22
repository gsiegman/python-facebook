from django.db import models

from django.contrib.auth.models import User

from facebook.graph import Graph


class FacebookProfile(models.Model):
    user = models.OneToOneField(User)
    facebook_id = models.CharField(max_length=25)
    access_token = models.CharField(max_length=255)
    dob = models.DateField(blank=True, null=True)
    
    def __unicode__(self):
        return u"%s (%s)" % (self.user.username, self.facebook_id,)
    
    @property
    def friends(self):
        g = Graph(str(self.access_token))
        return g.get_user_friends()
    
