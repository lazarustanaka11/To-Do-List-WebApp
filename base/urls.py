from django.urls import path
from .views import AssignmentList, AssignmentDetail, CreateAssignment, UpdateAssignment, DeleteAssignment, MySignInView, SignUp
from django.contrib.auth.views import LogoutView

urlpatterns= [
    path('', AssignmentList.as_view(), name='assignments'),
    path('sign-in/', MySignInView.as_view(), name='sign-in'),
    path('sign-out/', LogoutView.as_view(next_page= 'sign-in'), name= 'sign-out'),
    path('sign-up/', SignUp.as_view(), name= 'sign-up'),
    path('assignment/<int:pk>/', AssignmentDetail.as_view(), name='assignment'),
    path('create-assignment/', CreateAssignment.as_view(), name='create-assignment'),
    path('update-assignment/<int:pk>', UpdateAssignment.as_view(), name='update-assignment'),
    path('delete-assignment/<int:pk>', DeleteAssignment.as_view(), name='delete-assignment')
]