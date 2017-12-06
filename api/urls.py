from django.conf.urls import url, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'guitar_chords', views.GuitarChordViewSet)
router.register(r'users', views.UserViewSet)

schema_view = get_schema_view(title='Chordify API')

# API Endpoints
urlpatterns = [

    url('^schema/$', schema_view),

    url(r'', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]