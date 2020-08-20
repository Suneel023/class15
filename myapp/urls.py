from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
    path('multi/',views.multi,name="multiselect"),
]
