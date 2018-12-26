from django.urls import path

from . import views

urlpatterns = [
    path('insights/', views.ListInsights.as_view()),
    path('categories/', views.ListCategories.as_view()),
    path('insights/<int:pk>/', views.DetailInsight.as_view()),
]

# exapmles:
#   http://localhost:8000/api/v1/insights/?category=Environment
#   http://localhost:8000/api/v1/insights/1/
#   http://localhost:8000/api/v1/categories/