from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('topics/<int:topic_id>', views.topic, name='topic'),
    path('add_topic', views.add_topic, name='add_topic'),
    path('edit_topic/<int:topic_id>', views.edit_topic, name='edit_topic')
]