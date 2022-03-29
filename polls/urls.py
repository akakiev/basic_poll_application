from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # path('', views.index, name='index'), first variant
    # path('<int:question_id>/', views.detail, name='detail'), second variant
    # path('<int:question_id>/results/', views.results, name='results'), third variant
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]