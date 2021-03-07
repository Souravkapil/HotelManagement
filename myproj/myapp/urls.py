from django.urls import path
from .import views


urlpatterns = [
	
	  
      path('', views.signup, name="signup"),
      path('login', views.login, name="login"),
      path('index', views.index, name="index"),
      path('about', views.about, name="about"),
      path('room', views.room, name="room"),
      path('gallery', views.gallery, name="gallery"),
      path('reservation', views.reservation, name="reservation"),
      path('contact', views.contact, name="contact"),
      path('contactValue',views.contactValue,name='contactValue'),
      path('reservationvalue',views.reservationvalue,name='reservationvalue'),
      path('signup_data',views.signup_data,name='signup_data'),
      path('login_data',views.login_data,name='login_data'),

]