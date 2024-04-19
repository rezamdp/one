# ----> genrel imports <----
from django.contrib import admin
from account.models import User

# ----> extrenal imports <----
from .models import *


# -----> class CourierAdmin <-----
class CourierAdmin(admin.ModelAdmin):
    list_display = ('first_name_courier','last_name_courier','phone_number_courier')
admin.site.register(Courier , CourierAdmin )



# -----> ReasonAdmin <-----
admin.site.register(ReasonBack)


#======================================>ReportCourier Admin <======================================
class ReportCourierAdmin(admin.ModelAdmin):
    list_display = ('create_report' , )

admin.site.register(ReportCuorier , ReportCourierAdmin)

