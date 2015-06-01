from django.conf.urls import url
from views import CaptureUploadView


urlpatterns = [
    #Devices
    url(r'^api/captures/$', CaptureUploadView.as_view(), name='capture-upload'),
]