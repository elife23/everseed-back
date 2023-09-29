from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Commentmeeting)
admin.site.register(Commentwhiteboard)
admin.site.register(Meeting)
admin.site.register(Meetingroom)
admin.site.register(Participant)
admin.site.register(Subscription)
admin.site.register(User)
admin.site.register(Usersubscription)
admin.site.register(Whiteboard)
