from . import views
from django.urls import path

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('task-list/', views.task_list, name="task-list"),
    path('task-detail/<str:pk>/', views.task_detail, name="task-detail"),
    path('task-create/', views.task_create, name="task-create"),
    path('task-update/<str:pk>/', views.task_update, name="task-update"),
    path('task-delete/<str:pk>/', views.task_delete, name="task-delete"),
]