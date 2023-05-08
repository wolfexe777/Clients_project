from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'clients'

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('new/', views.client_new, name='client_create'),
    path('<int:pk>/', views.client_detail, name='client_detail'),
    path('<int:pk>/edit/', views.client_edit, name='client_edit'),
    path('<int:pk>/delete/', views.client_delete, name='client_delete'),
    path('search/', views.client_search, name='client_search'),
    path('client/<int:pk>/photo/', views.client_photo, name='client_photo')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)