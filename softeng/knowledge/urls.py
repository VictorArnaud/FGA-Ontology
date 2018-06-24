from django.urls import path
from .views import swebok

app_name = 'knowledge'

urlpatterns = [
    # swebok/
    path(
        "swebok/",
        swebok.SwebokListView.as_view(),
        name='swebok-list'
    ),
    # swebok/<slug>/details/
    path(
        "swebok/<slug:slug>/details/",
        swebok.SwebokDetailView.as_view(),
        name="swebok-detail"
    ),
    # swebok/<slug>/<topic>/details/
    path(
        "swebok/<slug:slug>/<slug:topic>/details/",
        swebok.TopicDetailView.as_view(),
        name="topic-detail"
    ),
]
