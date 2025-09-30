from django.urls import path
# from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, LikeView
from django.urls import include
urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    # path('members/', include('members.urls')),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_category', AddCategoryView.as_view(), name='add_category'),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/remove/<int:pk>', DeletePostView.as_view(), name="delete_post"),
    path('category/<int:cats>', CategoryView, name='category'),
    path('like/<int:pk>', LikeView, name='like_post'),



]
