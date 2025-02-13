from django.contrib import admin

from crudapp.models import User,AccessToken


# Register your models here.
admin.site.register(User)
admin.site.register(AccessToken)