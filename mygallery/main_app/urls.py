from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'),  
    path('about/', views.about, name='about'),  
    path('sculptures/', views.sculpture_index, name='sculpture-index'),
    path('sculptures/<int:sculpture_id>/', views.sculpture_detail, name='sculpture-detail'),
    # path('sculpture/edit/<int:id>/', views.sculpture_edit, name='sculpture-edit'),
    # path('sculpture/delete/<int:id>/', views.sculpture_delete, name='sculpture-delete'),
]
