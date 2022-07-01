

from django.contrib import admin
from django.urls import path,include
from schema_graph.views import Schema


from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view




urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("restaurant.urls")),
    path("schema/" ,Schema.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('openapi', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),

  

]
