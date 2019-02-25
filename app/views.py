from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = 'app/index.html'

class AboutView(TemplateView):
    template_name = 'app/about-us.html'

class CourseDetailView(TemplateView):
    template_name = 'app/course-details.html'

class CourseView(TemplateView):
    template_name = 'app/courses.html'
