from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import Course, Team


class HomeView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'home'

        course = Course.objects.all()
        context['course'] = course

        team = Team.objects.all()
        context['team'] = team

        return context

class AboutView(TemplateView):
    template_name = 'app/about-us.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'about-us'

        return context

class CourseDetailView(DetailView):
    template_name = 'app/course-details.html'
    model = Course

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'courses'

        return context

class CourseView(TemplateView):
    template_name = 'app/courses.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'courses'

        courses = Course.objects.all()
        context['courses'] = courses

        return context

class ElementView(TemplateView):
    template_name = 'app/elements.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'elements'

        return context

class ContactView(TemplateView):
    template_name = 'app/contact.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'contact'

        return context
