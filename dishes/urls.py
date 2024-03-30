from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'dishes'
urlpatterns = [
    path('', views.simple_view, name="index"),
    path('recipe/<slug:dish_address>', views.recipe_view, name='recipe')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
