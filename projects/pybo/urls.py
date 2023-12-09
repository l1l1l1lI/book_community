from django.urls import path
from .views import base_view
app_name = 'pybo'


urlpatterns = [
    # base_views.py
    path('', base_view.index, name='index'),
    path('<int:book_id>/', base_view.detail, name='detail'),

]
