from django.contrib import admin
from webapp.models import full_runner
from webapp.models import half_runner
from webapp.models import contact

# Register your models here.
admin.site.register(full_runner)
admin.site.register(half_runner)
admin.site.register(contact)
