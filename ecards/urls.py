from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = "ecards"
urlpatterns = [
    path('', views.CardList.as_view(), name="list"),
    path('/<str:ref_code>', views.CardDetails.as_view(), name="details"),
]
urlpatterns = format_suffix_patterns(urlpatterns)