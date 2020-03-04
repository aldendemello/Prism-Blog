from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from .views import AnnounceListView, AnnounceDetailView, AnnounceCreateView, AnnounceUpdateView, AnnounceDeleteView, UserAnnounceListView
from . import views

urlpatterns = [
    #path('', views.home, name='site-home'),
    path('about/', views.about, name='site-about'),
    path('faq/', views.faq, name='site-faq'),
    path('release/', views.release, name='site-release'),
    path('calendar/', views.calendar, name='site-calendar'),
    path('media/', views.media, name='site-media'),
    path('user/<str:username>', UserPostListView.as_view(), name='site-blog-user-posts'),
    path('blog/', PostListView.as_view(), name='site-blog'),
    path('blog/post/<int:pk>/', PostDetailView.as_view(), name='site-post-detail'),
    path('blog/post/new/', PostCreateView.as_view(), name='site-post-create'),
    path('blog/post/<int:pk>/update/', PostUpdateView.as_view(), name='site-post-update'),
    path('blog/post/<int:pk>/delete/', PostDeleteView.as_view(), name='site-post-delete'),
    path('announcement/user/<str:username>', UserAnnounceListView.as_view(), name='site-user-announcements'),
    path('', AnnounceListView.as_view(), name='site-home'),
    path('announcement/<int:pk>/', AnnounceDetailView.as_view(), name='site-announcements-detail'),
    path('announcement/new/', AnnounceCreateView.as_view(), name='site-announcements-create'),
    path('announcement/<int:pk>/update/', AnnounceUpdateView.as_view(), name='site-announcements-update'),
    path('announcement/<int:pk>/delete/', AnnounceDeleteView.as_view(), name='site-announcements-delete'),

]
