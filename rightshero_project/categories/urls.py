from django.urls import path
from . import views

urlpatterns = [
    path('category-selection/', views.category_selection_view, name='category_selection'),
    path('load-subcategories/', views.load_subcategories, name='load_subcategories'),
]
