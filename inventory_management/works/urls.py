"""works URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('invoice/melt/', views.invoice_generator_melt, name='invoice_generator_melt'),
    path('invoice/assembly/', views.invoice_generator_assembly, name='invoice_generator_assembly'),
    path('invoice/get/', views.get_code_values, name='get_code_values'),
    path('invoice/get/hsc/', views.get_hsc_values, name='get_hsc_values'),
    path('invoice/pdf/assembly/', views.generate_pdf_assembly, name='generate_pdf_assembly'),
    path('invoice/pdf/', views.generate_pdf, name='generate_pdf'),
    path('get/pdf/assembly/', views.get_pdf_assembly, name='get_pdf_assembly'),
    path('get/pdf/', views.get_pdf, name='get_pdf'),
    path('admin/', views.admin, name='admin'),
    path('admin/edit/<id>/', views.admin_edit, name='admin_edit'),
    path('admin/delete/<id>/', views.admin_delete, name='admin_delete'),
    path('admin/hsc/', views.hsc, name='hsc'),
    path('admin/hsc/edit/<id>/', views.hsc_edit, name='hsc_edit'),
    path('admin/hsc/delete/<id>/', views.hsc_delete, name='hsc_delete'),
    path('challan/', views.challan_no, name='challan_no'),
    path('challan/edit/<id>/', views.challan_no_edit, name='challan_edit'),
    path('', views.homepage, name='homepage'),
]