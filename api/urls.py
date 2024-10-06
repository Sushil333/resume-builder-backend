from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'profile', ProfileViewSet)
router.register(r'profile-skills', ProfileSkillViewSet)
router.register(r'resumes', ResumeViewSet)
router.register(r'experiences', ExperienceViewSet)
router.register(r'education', EducationViewSet)
router.register(r'achievements', AchievementViewSet)
router.register(r'certifications', CertificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# Register other viewsets here (e.g., resumes, profiles, etc.)