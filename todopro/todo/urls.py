from django.urls import path
from .views import Tasklist,TaskCreate,TaskUpdate,TaskDelete,TaskDetailView,CustomLogin,signup
from . import views

urlpatterns =[
    path('signup/',views.signup,name='signup'),
    path('login/',CustomLogin.as_view(),name='login'),
    path('task-list', Tasklist.as_view(),name= 'item'),
    path('create-task',TaskCreate.as_view(),name='create-task'),
    path('update-task/<int:pk>/',TaskUpdate.as_view(),name='update-task'),
    path('delete-task/<int:pk>/',TaskDelete.as_view(),name='delete-task'),
    path('details-task/<int:pk>/',TaskDetailView.as_view(),name='detail-task')
]