from django.urls import path


from .views import ToDoListView, ToDoDeatilView




urlpatterns = [
    path('todo_list/', ToDoListView.as_view()),
    path('todo_detail/<int:pk>/', ToDoDeatilView.as_view()),
]