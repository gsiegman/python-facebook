from django.contrib import admin

from facebook.extras.django.facebook.models import FacebookProfile


class FacebookProfileAdmin(admin.ModelAdmin):
    list_display = ["facebook_id", "user"]
    search_fields = ["facebook_id", "user"]

admin.site.register(FacebookProfile, FacebookProfileAdmin)
