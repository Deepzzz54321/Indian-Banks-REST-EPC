from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView
from . import views

app_name = 'banksapi'

urlpatterns = [
    path('', TemplateView.as_view(template_name='banksapi/index.html'), name='index'),
    path('banks/', views.BanksList.as_view()),
    path('banks/branches/', views.BranchesList.as_view()),
    path('banks/<int:id>/', views.BanksDetail.as_view()),
    path('banks/branches/ifsc=<str:id>/', views.BranchesIFSCDetail.as_view()),
    path('banks/branches/name=<str:name>&city=<str:city>/', views.BranchesFilter.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)