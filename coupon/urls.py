from django.urls import path


from coupon.views import (
    CouponListViewSet
)

coupon_list = CouponListViewSet.as_view({
    'get': 'list',
})

urlpatterns = [
    path('', coupon_list, name='coupon_list'),
]