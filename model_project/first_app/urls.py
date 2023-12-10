from django.urls import path
from .import views

urlpatterns = [
    path('', views.home , name= 'homePage' ),
    path('student_delete/<int:roll>',views.student_delete, name = "deleted_page")
]
