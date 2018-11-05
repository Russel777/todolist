from django.urls import path

from todolist_app import views

app_name = 'todolist_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.TodoCreateView.as_view(), name='add'),
    path('sign_up/', views.SignUpFormView.as_view(), name='sign_up'),
    path('sign_in/', views.SignInFormView.as_view(), name='sign_in'),
    path('sign_out/', views.SignOutView.as_view(), name='sign_out'),
    path('<int:pk>/', views.TodoDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', views.TodoDeleteView.as_view(), name='delete'),
]
