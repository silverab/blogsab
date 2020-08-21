from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from sports import views

urlpatterns = [	
    path('', views.home, name='home'),
    
    # path('profile/<int:pk>/', views.profile, name='profile'),
    # path('blog/single/', views.single, name='single'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)