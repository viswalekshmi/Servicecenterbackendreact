from django.urls import path
from api import views


urlpatterns=[

    path("customers/",views.CustomerListCreateView.as_view()),

    path("customers/<int:pk>/",views.CustomerRetrieveUpdateDestroyView.as_view()),

  
    path("customers/<int:pk>/work/",views.WorkCreateView.as_view()),

    path("work/<int:pk>/",views.WorkViewSet.as_view())

]