from django.contrib import admin
from django.urls import path, include
from lists import views as list_views
from lists import urls as list_urls

urlpatterns = [
    path('', list_views.home_page, name='nome'),
    path('lists/', include(list_urls),),
    #path('admin/', admin.site.urls),

]
