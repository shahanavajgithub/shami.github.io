from django.contrib import admin
from home.models import Contact # Shami Added(Registring the Model)
# Register your models here.

admin.site.register(Contact) # Shami Added(Registring the Model) without this you can't see contact entries
                             #  in "http://127.0.0.1:8000/admin"



