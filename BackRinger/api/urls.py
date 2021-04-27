from django.urls import path, include,re_path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('inventory',InvenViewSet)
router.register('curr',CurrViewSet)
router.register('bank',BankViewSet)
router.register('item',ItemViewSet)
router.register('price',PriceViewSet)
router.register('userdata',UserDataViewSet)
router.register('inven',InvenViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
    # path('address/', address_list),
    # path('users/',user_list),
    # path('curr/',curr_list),
    # path('curr/<str:pk>/',cur_details),
    # re_path(r'^(?:.*)/?$',index,name='Index')
]
