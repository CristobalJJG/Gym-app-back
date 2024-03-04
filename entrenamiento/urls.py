from django.urls import path
from . import views

urlpatterns = [
    path('', views.start),
    path('training/new/', views.create_new_training, name='create_a_new_trainning'),
    path('trainings/', views.get_all_trainings, name='get_all_trainnings'),
    path('training/<int:training_id>/', views.get_training_by_id, name='get_trainning_by_id'),
    path('training/patch/<int:training_id>/', views.update_training_by_id, name='update_trainnings_by_id'),
    path('training/delete/<int:training_id>/', views.delete_training_by_id, name='delete_trainnings_by_id'),
]