from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('<slug:post>/', views.post_single, name='post_single'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)