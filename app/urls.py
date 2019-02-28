from django.urls import path

from app.views import CourseDetailView
app_name = 'app'

urlpatterns = [
    path('coursedetail/<int:pk>/', CourseDetailView.as_view(),name = 'course_details'),
]