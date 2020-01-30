from django.urls import path
from . import views
urlpatterns = [
    path('', views.IndexView.as_view(), name='aktualnosci'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('post/', views.postview, name='post'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('', views.aktualnosci, name='aktualnosci'),
    path('sekcje', views.sekcje, name='sekcje'),
    path('harmonogram', views.harmonogram, name='harmonogram'),
]
