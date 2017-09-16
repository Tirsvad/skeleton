from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from . import views

urlpatterns = [
]

urlpatterns += i18n_patterns(
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomeView.as_view(), name='home'),
)
