from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'user', views.UserViewSet)

# The API URLs are not determined automatically by the router
urlpatterns = [
    path('', include(router.urls))
]