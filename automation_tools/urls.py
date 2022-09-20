"""automation_tools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Automation Tools API",
        default_version='v1',
        description="API for Automation Tools",
        terms_of_service="https://github.com/shamspias/Automation-Tools",
        contact=openapi.Contact(email="shamsuddinpias0@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger'),

    path('blog/', include('auto_blog_writer.urls'), name='ai-blog-writer'),
    path('proof-reader/', include('ai_proofreader.urls'), name='ai-proofreader'),
    path('translate/', include('document_translator.urls'), name='document-translator'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# django admin customization
admin.site.site_header = 'Automation Works Admin'
admin.site.site_title = 'Automation Works Admin Portal'
admin.site.index_title = 'Welcome to Automation Works Admin Portal'
