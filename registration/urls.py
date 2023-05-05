from django.urls import path
from .views import Registration, uservalidation,phonevalidation,emailvalidation,Login,Logout



urlpatterns = [
   path('', Registration.as_view(), name="register"),
   path('usernamevalide',uservalidation, name='usernamevalid' ),
   path('phonevalide',phonevalidation, name='phonevalid' ),
   path('emailvalide',emailvalidation, name='emailvalid' ),
   # path('passwordvalide',emailvalidation, name='passwordvalid' ),
   path('login', Login.as_view(), name="login"),
   path('logout',Logout.as_view(), name='logout' )
   
   
   
]
