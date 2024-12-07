from django.urls import path
from . import views  

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),  
    path('accounts/signup/', views.signup, name='signup'),
    path('sculptures/', views.sculpture_index, name='sculpture-index'),
    path('sculptures/<int:sculpture_id>/', views.sculpture_detail, name='sculpture-detail'),
    path('sculptures/create/', views.SculptureCreate.as_view(), name='sculpture-create'),
    path('sculptures/<int:pk>/update/', views.SculptureUpdate.as_view(), name='sculpture-update'),
    path('sculptures/<int:pk>/delete/', views.SculptureDelete.as_view(), name='sculpture-delete'),
]
