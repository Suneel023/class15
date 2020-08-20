from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
    path('multi/',views.multi,name="multiselect"),
    path('img_upl/',views.img_upload,name="img_upload"),
    path('img_displ/',views.img_display,name="img_disp"),
]
