from rest_framework.routers import DefaultRouter
from exam_management_app import views
from django.urls import path, include

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'branches', views.BranchViewSet, basename='branch')
router.register(r'streams', views.StreamViewSet, basename='stream')
router.register(r'colleges', views.CollegeViewSet, basename='college')

urlpatterns = [
    path('', include(router.urls)),
]