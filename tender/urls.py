from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashborad, name='dashborad'),
    path('all/', views.all, name='all'),
    path('bid/<str:pk_bid>', views.bidedit, name='bidedit'),
    path('bid/view/<str:pk_bid>', views.bidview, name='bidview'),
    path('active/', views.active, name='active'),
    path('inactive/', views.inactive, name='inactive'),
    path('applied/', views.applied, name='applied'),
    path('unapplied/', views.unapplied, name='unapplied'),
    path('won/', views.won, name='won'),
    
    # path('add', views.add, name='add'),
]
