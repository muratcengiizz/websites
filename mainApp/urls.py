from django.urls import path 
from . import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [ 
    path("", views.index, name="index"),
    path("hakkimda", views.hakkimda, name="hakkimda"),
    path("yazilar", views.yazilarr, name="yazilar"),
    path("iletisim", views.iletisimm, name="iletisim"),
    
    path('yazilar/yazi1', views.yazi1, name="yazi1"),
    path('yazilar/yazi2', views.yazi2, name="yazi2"),
    path('yazilar/yazi3', views.yazi3, name="yazi3"),
    path('yazilar/yazi4', views.yazi4, name="yazi4"),
    path('yazilar/yazi5', views.yazi5, name="yazi5")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 