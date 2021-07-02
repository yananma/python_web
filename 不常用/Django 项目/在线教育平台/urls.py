from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('course', views.course, name='course'),
    path('vip', views.vip, name='vip'),
    path('test', views.test, name='test'),
    path('test1', views.test1, name='test'),
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('comment/<int:bid>', views.CommentView.as_view(), name='comment'),
    path('logout', views.my_logout, name='logout'),
    path('blog-list', views.blog_list, name='blog-list'),
    path('blog-detail/<int:bid>', views.blog_detail, name='blog-detail'),
    path('tag/<int:tid>', views.tag, name='tag'),
    path('course-detail/<int:cid>', views.course_detail, name='course-detail'),
    path('comment_del/<int:id>/<int:bid>',views.comment_del, name='comment_del'),
    path('comment_update/<int:id>/<int:bid>',views.comment_update, name='comment_update'),
    # path('com_update/<int:pk>',views.CommentUpdate.as_view(), name='com_update'),

]
