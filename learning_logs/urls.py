"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Home page
    path('', views.index, name = 'index'),
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Page that shows information about author.
    path('aboutMe/', views.aboutMe, name ='aboutMe'),
    # Page that shows contact information.
    path('contactMe/', views.contactMe, name='contactMe'),
    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),

]
