
from django .urls import path
from . import views

urlpatterns = [
    path('create/',views.home),
    path('',views.user),
    path('detailuser/<int:user_id>/', views.detailuser,name='details'),
    path('updateuser/<int:user_id>/',views.updateuser,name='update'),
    path('deleteuser/<int:user_id>/', views.deleteuser,name='delete')
]
