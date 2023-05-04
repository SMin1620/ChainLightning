from django.urls import path


from coupon.views import (
    CouponListViewSet
)

coupon_list_create = CouponListViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

urlpatterns = [
    path('', coupon_list_create, name='coupon_list_create'),
]