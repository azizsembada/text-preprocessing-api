from django.conf.urls import url


from .preprocessing import (
    PreprocessingAPIView, 
    ) 


urlpatterns = [
    url(r'^$', PreprocessingAPIView.as_view()),
]