from django.urls import path

from . import views
from polls.views import deep_view, list_view


app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('deepthoughts', deep_view),
    path('deepthoughts/list', list_view)
]