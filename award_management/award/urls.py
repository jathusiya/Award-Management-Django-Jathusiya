from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('school/', views.school, name="school"),
    path('subject/', views.subject, name="subject"),
    path('student/', views.student, name="student"),
    path('award/', views.award, name="award"),
    path('answer/', views.answer, name="answer"),
    path('classes/', views.classes, name="classes"),
    path('assessment/', views.assessment, name="assessment"),
    path('summary/', views.summary, name="summary"),
]
