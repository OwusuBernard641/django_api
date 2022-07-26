from django.urls import path
from .import views

urlpatterns =[
    path('',views.apiOverview,name='api-overview'),
    path('task-list/',views.tasklist,name='task-list'),
    path('task-detail/<str:pk>/',views.taskDetail,name='task-detail'),
    path('task-create/',views.taskCreate,name='task-create'),
    path('task-update/<str:pk>/',views. taskUpdate,name='task-update'),
    path('task-delete/<str:pk>/',views. taskDelete,name='task-Delete'),
    
    
    path('order-list/',views.orders,name='order-list'),
    path('register-person/',views.registerperson,name='register-person'),
    path('login-person/<str:pk>/',views.login,name='login-person'),
    path('dish-detail/<str:pk>/',views.dishDetail,name='dish-detail'),
    path('restaurant-list/',views.restaurantlist,name='restaurant-list'),
    path('person-list/',views.personlist,name='person-list'),
    path('dispatch-on<str:pk>/',views.dispatchOn,name='dispatch-on'),
    path('dispatch-off<str:pk>/',views.dispatchOff,name='dispatch-off'),
    path('dispatch-list/',views.dispatchlist,name='dispatch-list'),
    path('send-order<str:pk>/',views.sendOrder,name='send-order'),
    
]