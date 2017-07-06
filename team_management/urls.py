from django.conf.urls import url

from members import views

urlpatterns = [
    url(r'^members/$', views.MemberList.as_view()),
    url('^members/(?P<pk>[0-9]+)/$', views.MemberDetail.as_view()),
]
