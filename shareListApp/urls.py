from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='onboarding'),
    path('userlogin/',views.userlogin, name='user_login'),
    path('userlist/',views.userlist, name='user_list'),

    # path('addshares/',views.addshares, name='add_shares'),
    path('addshares/<int:id>',views.addshares, name='add_shares'),

    path('shareslist/<int:id>',views.shareslist, name='shares_list'),
    path('shareslist/<int:s_id>/<int:id>',views.shareslist, name='shares_list'),
        
    path('delete/<int:s_id><int:id>',views.deleteshare, name='delete_share'),
]