from django.contrib import admin



from .models import *

admin.site.register(Store)
admin.site.register(Customer)
admin.site.site_header = 'Store Admin'
