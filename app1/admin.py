from django.contrib import admin
from .models import Users, Entry, Party, Agent, Transport, Viewer
# Register your models here.
admin.site.register(Users)
admin.site.register(Entry)
admin.site.register(Party)
admin.site.register(Agent)
admin.site.register(Transport)
admin.site.register(Viewer)
