from django.contrib import admin

# Register your models here.
from .models import Users

class userAdmin(admin.ModelAdmin):
    list_display = ('username', 'usercode','userclass','usergrade')
admin.site.register(Users, userAdmin)