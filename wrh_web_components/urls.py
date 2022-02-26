from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import AllowAny
from rest_framework.renderers import DocumentationRenderer
from rest_framework.schemas import get_schema_view

class CustomRenderer(DocumentationRenderer):
    languages = ['python']
    # template = 'docs/index.html'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("apps.zwift_components.urls")),
    path('schema', get_schema_view(
            title="ZwiftApi",
            description="API for all things …",
            version="1.0.0"
        ), name='openapi-schema'),
    path('', include_docs_urls(title='WRH - Web Components API`s', permission_classes=[AllowAny],
                               renderer_classes=[CustomRenderer])),
]
