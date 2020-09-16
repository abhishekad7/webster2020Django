
from django.urls import path, include
from .import views as quizviews

urlpatterns = [
    path('', quizviews.index, name='quiz_index'),
    path('create-poll/', quizviews.createPoll, name='create_poll'),
]
