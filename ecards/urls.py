from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = "ecards"
urlpatterns = [
    path('', views.card_list, name="list"),
    path('api/v1/cards', views.CardList.as_view(), name="api_list"),
    path('api/v1/cards/<str:ref_code>',
         views.CardDetails.as_view(), name="api_details"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
