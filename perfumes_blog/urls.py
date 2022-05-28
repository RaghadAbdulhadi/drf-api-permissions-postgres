from django.urls import path
from perfumes_blog.api.viewsets import PerfumesDetailView, PerfumesListView
urlpatterns = [
    path('perfumes-list', PerfumesListView.as_view(), name='perfumes_list'),
    path('perfume-detail/<int:pk>', PerfumesDetailView.as_view(), name='perfumes_detail'),
]