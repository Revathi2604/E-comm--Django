from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
     path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),

    path('home/', views.home, name='home'),
   
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact/', views.contact, name='contact'),




   path('login/', views.login, name='login'),
   path('signup/', views.signup, name='signup'),



    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),



     path('register/', views.register, name='register'),
     path('login/', views.login, name='login'),





      path('main/', views.join_view, name='main'),  # Replace 'join_view' with the correct view function






     path('join/', views.join_view, name='join'),


     path('access/', views.access_view, name='access'),

     path('access/', views.login_view, name='access'),














]

