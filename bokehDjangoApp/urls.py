from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.graph, name="graph"),
    path('learnGraph', views.graph2, name="graph2"),
    path('combo', views.combo, name="combo"),
    path('pop', views.pop, name="pop"),
    path('products', views.products, name="products"),
]
