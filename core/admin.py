from django.contrib import admin

# Register your models here.
from core.models import Issue, Type

admin.site.register(Issue)
admin.site.register(Type)
