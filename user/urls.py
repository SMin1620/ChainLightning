from django.urls import path

from user.views import (
    UserCouponViewSet
)


user_coupon = UserCouponViewSet.as_view({
    'post' : 'create'
})


urlpatterns = [
    path('charge/', user_coupon, name='charge'),
]