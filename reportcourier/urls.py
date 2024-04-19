from django.urls import path
from .views import *

app_name = 'reportcourier'
urlpatterns = [
    path('dashboard_home/', ListReportCourierView.as_view(), name='dashboard_home'),
    path('add_reasonback/', CreateReasonBackView.as_view(), name='add_reasonback'),
    path('update_reasonback/<int:pk>', UpdateReasonBackView.as_view(), name='update_reasonback'),
    path('delete_reasonback/<int:pk>', UpdateReasonBackView.as_view(), name='delete_reasonback'),
    path('add_courier/', CreateCourierView.as_view(), name='add_courier'),
    path('update_courier/<int:pk>', UpdateCourierView.as_view(), name='update_courier'),
    path('delete_courier/<int:pk>', DeleteCourierView.as_view(), name='delete_courier'),
    path('add_reportcourier/', CreateReportCourierView.as_view(), name='create_reportcourier'),
    path('update_reportcourier/<int:pk>', UpdateReportCourierView.as_view(), name='update_reportcourier'),
    path('detail_reportcourier/<int:pk>', DetailReportCourierView.as_view(), name='detail_reportcourier'),
    path('delete_reportcourier/<int:pk>', DeleteReportCourierView.as_view(), name='delete_reportcourier'),

]

# --->  href = {% url "reportcourier  : dashboard_home %}

# pattern url site ----> test.com/app/views
