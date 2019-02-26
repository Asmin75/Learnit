from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'home'

class AboutView(TemplateView):
    template_name = 'app/about-us.html'

    def get_context_data(self,**kwargs):
        context = get_context_data(**kwargs)
        context['active'] = 'about-us'

class CourseDetailView(TemplateView):
    template_name = 'app/course-details.html'

    def get_context_data(self,**kwargs):
        context = get_context_data(**kwargs)
        context['active'] = 'course-details'

class CourseView(TemplateView):
    template_name = 'app/courses.html'

    def get_context_data(self,**kwargs):
        context = get_context_data(**kwargs)
        context['active'] = 'courses'

class ElementView(TemplateView):
    template_name = 'app/elements.html'

    def get_context_data(self,**kwargs):
        context = get_context_data(**kwargs)
        context['active'] = 'elements'

class ContactView(TemplateView):
    template_name = 'app/contact.html'

    def get_context_data(self,**kwargs):
        context = get_context_data(**kwargs)
        context['active'] = 'contact'
