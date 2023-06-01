from django.urls import path
from .views import NewsList, PieceOfNewsDetail


urlpatterns = [
   path('', NewsList.as_view()),
   path('<int:pk>', PieceOfNewsDetail.as_view())
]