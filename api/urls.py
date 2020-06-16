
from django.contrib import admin
from django.conf.urls import include, url


# urls
urlpatterns = [
    url(r'^', include('todos.urls')),
    url(r'^admin/', admin.site.urls),
]