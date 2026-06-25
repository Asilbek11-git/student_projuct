from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CourseForm


@login_required
@permission_required("courses.add_course", raise_exception=True)
def course_create(request):
    if request.method == 'POST':
         form = CourseForm(request.POST)
         if form.is_valid():
             form.save()
    return render(request, 'courses/course_form.html')

        
 


@login_required
def course_list(request):
    return render(request, 'courses/course_list.html')