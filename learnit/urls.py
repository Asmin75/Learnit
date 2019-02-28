"""learnit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from app.views import HomeView, AboutView, CourseDetailView, CourseView, ElementView, ContactView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name ='home'),
    path('about/',AboutView.as_view(), name = 'about-us'),
    # path('coursedetail/',CourseDetailView.as_view(), name = 'course-details'),
    path('', include('app.urls')),
    path('course/',CourseView.as_view(), name = 'courses'),
    path('elements/',ElementView.as_view(), name = 'elements'),
    path('contact/',ContactView.as_view(), name = 'contact'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
