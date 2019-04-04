from django.contrib import admin
from portfolio.models import AnalogProject
from portfolio.models import DigitalProject
# Register your models here.

admin.site.register(AnalogProject)
admin.site.register(DigitalProject)