"""recenzent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from film import views as film_views
from newsy import views as newsy_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', film_views.home, name='home'),
    path('about/', film_views.about, name='about'),

    path('newsy/', newsy_views.newsy, name='newsy'),
    path('newsy/<int:news_id>/', newsy_views.newsy_detail, name='newsy_detail')


]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)