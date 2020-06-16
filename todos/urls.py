from django.urls import include, path, re_path
from . import views


urlpatterns = [
    re_path(r'^api/v1/todos/(?P<pk>[0-9]+)$', # Url to get update or delete a todo
        views.get_delete_update_todo.as_view(),
        name='get_delete_update_todo'
    ),
    path('api/v1/todos/', # urls list all and create new one
        views.get_post_todos.as_view(),
        name='get_post_todos'
    )
]