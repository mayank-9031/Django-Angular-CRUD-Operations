# from django.urls import path
# from .views import UserList, UserDetail, helloWorld, MyTokenObtainPairView
# from rest_framework_simplejwt.views import TokenRefreshView

# urlpatterns = [
#     path('users/', UserList.as_view(), name="user-list"),
#     path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
#     path('hello/', helloWorld, name='hello-world'),
#     path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]


# from django.urls import path
# from .views import UserList, UserDetail, helloWorld, MyTokenObtainPairView, LogoutView, TokenRefreshView

# urlpatterns = [
#     path('users/', UserList.as_view(), name="user-list"),
#     path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
#     path('hello/', helloWorld, name='hello-world'),
#     path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('logout/', LogoutView.as_view(), name='token_blacklist'),
# ]



from django.urls import path
from .views import UserList, UserDetail, helloWorld, MyTokenObtainPairView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('users/', UserList.as_view(), name="user-list"),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('hello/', helloWorld, name='hello-world'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='token_blacklist'),
]





