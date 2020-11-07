from django.urls import path

from . import views
# app_name = 'user'
urlpatterns = [   
    path('home', views.home, name='home'),
    path('save', views.save_data, name='save'),
    path('delete', views.delete_data, name='delete'),
    path('edit', views.edit_data, name='edit'),

    path('recipe-add', views.RecipeCreateView.as_view(), name='recipe-add'),
]