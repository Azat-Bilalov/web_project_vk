from django.urls import path

from . import views

app_name = 'questions'

urlpatterns = [
    path('', views.index, name='index'),
    path('tag/<str:tag>', views.index, name='list_with_tag'),
    path('hot/', views.index, name='hot_list'),
    path('page/<int:page>', views.index, name='list_page'),
    path('ask/', views.new_question, name='new_question'),
    path('question/<int:id>/', views.question, name='question'),
    path('login/', views.sign_in, name='sign_in'),
    path('signup/', views.sign_up, name='sign_up'),
    path('settings/', views.settings, name='settings')
]
