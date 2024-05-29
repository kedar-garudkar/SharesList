from django.contrib import admin
from .models import UserDetails,ShareDetails

# Register your models here.
admin.site.register([UserDetails,ShareDetails])