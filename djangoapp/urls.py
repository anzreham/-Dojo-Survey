
from django.urls import path     
from . import views
urlpatterns = [
      path('', views.formpage),
      path('result', views.result),
#      path('blogs/', views.some_function ),
#      path('users',views.create_user),
#      path('success', views.success)
    
 
]