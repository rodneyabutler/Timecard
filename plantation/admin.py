from django.contrib import admin
from plantation.models import UserProfile
# Register your models here.



from django.contrib import admin
from plantation.models import Plantation, Route, Counties, Location

admin.site.register(Plantation)
admin.site.register(Route)
admin.site.register(Counties)
admin.site.register(Location)
admin.site.register(UserProfile)
