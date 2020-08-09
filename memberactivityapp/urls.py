from django.urls import path
from .views import (MemberCreateView,HomeView,
MemberDeleteView,MemberUpdateView,
MemberDetailView,ActivityCreateView,ApiView,ActivityUpdateView,ActivityDeleteView)

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('create-member/', MemberCreateView.as_view(),name='create-member'),
    path('delete-member/<uuid:pk>', MemberDeleteView.as_view(),name='delete-member'),
    path('detail-member/<uuid:pk>', MemberDetailView.as_view(),name='detail-member'),
    path('update-member/<uuid:pk>', MemberUpdateView.as_view(),name='update-member'),
    path('create-activity/<uuid:pk>', ActivityCreateView.as_view(),name='create-activity'),
    path('update-activity/<int:pk>', ActivityUpdateView.as_view(),name='update-activity'),
    path('delete-activity/<int:pk>', ActivityDeleteView.as_view(),name='delete-activity'),
    path('members-all/', ApiView.as_view(),name='api-view'),
    
]
