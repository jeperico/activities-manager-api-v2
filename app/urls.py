from django.urls import include, path
from drf_spectacular.views import (
  SpectacularAPIView,
  SpectacularRedocView,
  SpectacularSwaggerView,
)

urlpatterns = [
  path(
    'schema/',
    SpectacularAPIView.as_view(),
    name='schema'
  ),
  path(
    'schema/swagger/',
    SpectacularSwaggerView.as_view(url_name='schema'),
    name='swagger-ui'
  ),
  path(
    'schema/redoc/',
    SpectacularRedocView.as_view(url_name='schema'),
    name='redoc'
  ),
  path('profiles/', include('apps.profiles.urls'))
]