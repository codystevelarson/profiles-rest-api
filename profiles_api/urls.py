from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Setting the router to configure our view set paths
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
# Basename not needed when 'queryset' variable is included in the view set class
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
