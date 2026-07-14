from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'phrases', views.PhraseViewSet)
router.register(r'people', views.PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('seed/', views.seed_data, name='seed-data'),
]
