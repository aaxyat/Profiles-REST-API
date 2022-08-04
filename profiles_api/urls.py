from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router= DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-api/', views.HelloApiView.as_view(), name='hello-api'),
    path('login/', views.UserLoginApiView.as_view(), name='login-api'),
    path('', include(router.urls)),
]