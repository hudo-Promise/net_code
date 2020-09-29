from django.urls import path

from . import views

urlpatterns = [
    path('login', views.mylogin),
    path('test_session', views.test_session),
    path('show_session', views.show_session),
    path('reg', views.myregister),
    path('logout', views.mylogout),

]