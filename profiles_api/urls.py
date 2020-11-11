from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Setting the router to configure our view set paths
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
# Basename not needed when 'queryset' variable is included in the view set class
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    # Anything else default to the router's registered view sets
    path('', include(router.urls))
]
