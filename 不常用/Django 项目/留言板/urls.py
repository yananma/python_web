from . import views
from django.urls import path

urlpatterns = [
    path('del/<int:pk>', views.ContactDelete.as_view(), name='del'), 
    path('update/<int:pk>', views.ContactUpdate.as_view(), name='update'),
    path('list', views.ContactListView.as_view(), name='list'),
    path('create', views.ContactCreate.as_view(), name='create'),
]