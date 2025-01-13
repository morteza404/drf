from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import ArticleList, ArticleDetail, AuthorList, AuthorDetail

urlpatterns = [
    path("article/", ArticleList.as_view(), name="article"),
    path("article/<int:pk>/", ArticleDetail.as_view(), name="article-detail"),
    path("author/", AuthorList.as_view(), name="author"),
    path("author/<int:pk>/", AuthorDetail.as_view(), name="author-detail"),
     path("token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
]
