from django.urls import path
from . import views

urlpatterns=[ 
    path('register/',views.RegisterUser, name="register"),
    path('login/',views.LoginUser, name="login"),
    path('adminlogin/',views.LoginAdmin, name="adminlogin"),
    path('logout/',views.LogoutUser, name="logout"),
    path('',views.HomePage,name='home'),
    path('portfolios/',views.Portfolios,name='portfolios'),
    path('download/<str:pk>/',views.ViewPhoto,name='download'),
    path('addphoto/',views.AddPhoto,name='addphoto'),
    path('testimonials/',views.TestimonialsPage,name='testimonials'),
    path('booking/',views.Booking,name='booking'),
]