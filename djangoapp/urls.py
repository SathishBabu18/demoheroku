
from django.urls import path
from djangoapp import views #fbv
from .views import productreg,productlist,productdetail,productupdate,productdelete#cbv
urlpatterns = [
    path('home/',views.home,name='home'),
    path('Product/',views.Product,name='Product'),
    path('service/',views.service,name='service'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contact/',views.contact,name='contact'),
#FBV
    path('get_product/',views.get_product,name='get_product'),
    path('detail_product/<pk>',views.detail_product,name='detail_product'),
    path('update_product/<pk>',views.update_product,name='update_product'),
    path('delete_product/<pk>',views.delete_product,name='delete_product'),

#CBV
    path('productreg/', productreg.as_view(), name = 'productreg'),
    path('', productlist.as_view(), name = 'productlist'),
    path('<pk>/productdetail', productdetail.as_view(), name = 'productdetail'),
    path('<pk>/productupdate',productupdate.as_view(),name = 'productupdate'),
    path('<pk>/productdelete', productdelete.as_view(), name = 'productdelete'),
]


