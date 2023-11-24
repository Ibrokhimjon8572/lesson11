from django.urls import path
from .views import contents, post_detail, load

urlpatterns = [
    path('', contents, name='contents'),
    path('content/<int:pk>', post_detail, name='content'),
    path('load/', load, name='load_page'),
]