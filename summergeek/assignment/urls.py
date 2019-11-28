from . import views
from django.urls import path
import re
urlpatterns = [
    path('',views.index,name="entry"),
    path("result",views.result,name="sendFn"),
]