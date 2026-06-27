from django.urls import path
from .views import course_create,course_list_view




urlpatterns = [
    path('couse/',course_create,name='course_create'),
    path('', course_list_view, name='course_list')

]