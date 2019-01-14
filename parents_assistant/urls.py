from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.urls import path, include
from django.views.generic import TemplateView

from parents_assistant import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', include('home.urls')),
    path('manual/', TemplateView.as_view(template_name='user_manual/user-manual.html'), name='manual'),
    path('social/', include('social_django.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
