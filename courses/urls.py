from django.urls import path
from courses.views import course_create,course_list




urlpatterns = [
    path('couse/',course_create,name='course_create'),
    path('course_list/',course_list,name='course_list')

]