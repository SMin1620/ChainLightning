from django.urls import path

from pay.views import (
    UserPayViewSet
)

user_pay = UserPayViewSet.as_view({
    'post': 'create',
})


urlpatterns = [
    path('', user_pay, name='user_pay'),
]