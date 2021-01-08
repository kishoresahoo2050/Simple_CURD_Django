from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="home"),
    path('DelRecord/', views.DeleteRec,name="DelRec"),
    path('Edit/<int:edit_id>',views.Details,name="Edit")
]