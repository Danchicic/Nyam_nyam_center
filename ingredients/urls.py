from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'ingredients'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('succsful_update/', views.SuccessfulView.as_view(), name='successful')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
