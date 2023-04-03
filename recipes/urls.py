from django.urls import path, re_path
from recipes import views

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^(?P<type>cd|dd)\.(?P<drink_id>\w+)/$', views.recipe_detail, name='recipe-detail'),
    re_path(r'^(?P<type>cd|dd)\.(?P<drink_id>\w+)/save$', views.recipe_saver, name='recipe-save'),
    path('about', views.about, name='about'),
    path('advanced/', views.advanced_search, name='advanced_search'),
]