from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views #import this
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name = 'home'),
    path('restaurantHome/', views.restaurantHome, name = 'restaurantHome'),
    path('restaurants/', views.restaurants, name = 'restaurants'),
    path('search/', views.search, name = 'search'),
    path('contact/', views.contact, name = 'contact'),
    path('order/<str:pk>/', views.order, name = 'order'),
    path('reservation/<str:pk>/', views.reservation, name = 'reservation'),
    path('comment/<str:pk>/', views.comment, name = 'comment'),
    path('cancel_res/<str:pk>/', views.cancel_res, name = 'cancel_res'),
    path('cancel_order/<str:pk>/', views.cancel_order, name = 'cancel_order'),
    path('order_details/<str:pk>/', views.order_details, name = 'order_details'),
    path('reservation_details/<str:pk>/', views.reservation_details, name = 'reservation_details'),
    path('profile/', views.profile, name = 'profile'),
    path('menu/', views.menu, name = 'menu'),
    path('cancelOrder/<str:pk>/', views.cancelOrder, name = 'cancelOrder'),
    path('cancelRes/<str:pk>/', views.cancelRes, name = 'cancelRes'),
    path('acceptOrder/<str:pk>/', views.acceptOrder, name = 'acceptOrder'),
    path('acceptRes/<str:pk>/', views.acceptRes, name = 'acceptRes'),
    path('restaurantProfile/', views.restaurantProfile, name = 'restaurantProfile'),
    path('userLogin/', views.userLogin, name = 'userLogin'),
    path('restaurantLogin/', views.restaurantLogin, name = 'restaurantLogin'),
    path('restaurantRegister/', views.restaurantRegister, name = 'restaurantRegister'),
    path('logoutUser/', views.logoutUser, name = 'logoutUser'),
    path('userRegister/', views.userRegister, name = 'userRegister'),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)