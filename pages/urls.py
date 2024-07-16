from django.urls import path
from pages.views import HomePageView, ContactView, MatchPageView, TeamPageView, NewsPageView, NewsSinglePageView, \
    StorePageView

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contacts'),
    path('mathches/', MatchPageView.as_view(), name='matches'),
    path('staff/', TeamPageView.as_view(), name='staff'),
    path('news/', NewsPageView.as_view(), name='news'),
    path('news/<int:pk>/', NewsSinglePageView.as_view(), name='detail'),
    path('store/', StorePageView.as_view(), name='store')
]
