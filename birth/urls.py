from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('children_list', views.children_list, name='children-list'),
   
    
    path('add_father', views.add_father, name='add-father'),
    path('add_mother', views.add_mother, name='add-mother'),
    path('add_child', views.add_child, name='add-child'),
   

   
    path('update_child/<child_id>', views.update_child, name='update-child'),
    path('show_child/<child_id>', views.show_child, name='show-child'),
    path('search_child', views.search_child, name='search-child'),
]


