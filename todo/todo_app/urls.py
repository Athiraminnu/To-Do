from . import views
from django . urls import path

urlpatterns = [
    path('', views.demo, name='demo'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:taskid>/', views.update, name='update'),
    path('classview/', views.listing.as_view(), name='classview'),
    path('detailview/<int:pk>/', views.details.as_view(), name='detailview'),
    path('updateview/<int:pk>/', views.updateview.as_view(), name='updateview'),
    path('deleteview/<int:pk>/', views.deleteview.as_view(), name='deleteview'),
]
