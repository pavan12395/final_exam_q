from django.urls import path
from votes.views import home,result
urlpatterns=[
    path('<int:id>/',home),
    path('<int:id>/results/',result)
]