from django.urls import path
from . import views

urlpatterns= [
    path('',views.loginpage,name = 'loginpage'),
    path('authenticat/',views.authenticat.as_view(),name ='authenticat'),
    path('home/', views.home, name= 'home'),
    path('result/', views.result.as_view(), name= 'result'),
    path('predicte/', views.predicte.as_view(), name= 'predicte'),
    # path('predicte/result', views.predicte.as_view(), name= 'predicte'),
    path('report/',views.report, name= 'report'),
    path("newAccount/",views.newAccount,name='newAccount'),
    path('addUser/',views.addUser.as_view(),name ='addUser')
]
