from django.urls import path
#from .import views
from .views import HomeView,Article_DetailView
urlpatterns = [
#path('',views.home, name='home')
path('', HomeView.as_view(), name = "home" ),
path('article/<int:pk>', Article_DetailView.as_view(), name= "articledetail" ),
]
