from rest_framework import routers
from .views import ToDoView

route = routers.DefaultRouter()
route.register(r"api/todo", ToDoView, 'api')

urlpatterns = route.urls