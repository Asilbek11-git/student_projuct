from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CourseForm
from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Course, Category  











@login_required
@permission_required("courses.add_course", raise_exception=True)
def course_create(request):
    if request.method == 'POST':
         form = CourseForm(request.POST)
         if form.is_valid():
             form.save()
    return render(request, 'courses/course_form.html')

        
 







@login_required
def course_list_view(request):
    courses = Course.objects.all().order_by('-created_by')
    query = request.GET.get('search')
    if query:
        courses = courses.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    category_id = request.GET.get('category')
    if category_id:
        courses = courses.filter(category_id=category_id)
    paginator = Paginator(courses, 3) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()
    context = {
        'page_obj': page_obj,     
        'categories': categories, 
        'search_query': query,     
        'selected_category': category_id, 
    }
    
    return render(request, 'courses/course_list.html', context)