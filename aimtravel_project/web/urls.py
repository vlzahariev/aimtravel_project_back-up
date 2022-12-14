from django.urls import path, include

from aimtravel_project.web import views
from aimtravel_project.web.views import CreateOfferView, DisplayOfferView, AllEmployeeView, \
    DisplayAdditionalServicesView, EditOfferView, DeleteOfferView, DetailsOfferView, CreateCompanyView, AllCompanyView, \
    EditCompanyView, CompanyDetailView, DeleteCompanyView, DisplayPricesView, CreatePriceView, EditPriceView, \
    DeletePriceView, DetailsPriceView

urlpatterns = (
    path('', views.index, name='index'),
    path('admin_panel/', views.admin_panel, name='admin panel'),
    path('offer/', include([
        path('add/', CreateOfferView.as_view(), name='add offer'),
        path('offers/', DisplayOfferView.as_view(), name='offers'),
        path('edit/<int:pk>/', EditOfferView.as_view(), name='edit offer'),
        path('delete/<int:pk>/', DeleteOfferView.as_view(), name='delete offer'),
        path('details/<int:pk>/', DetailsOfferView.as_view(), name='details offer'),
    ])),
    path('prices/', include([
        path('add/', CreatePriceView.as_view(), name='add price'),
        path('display/', DisplayPricesView.as_view(), name='prices'),
        path('edit/<int:pk>/', EditPriceView.as_view(), name='edit price'),
        path('delete/<int:pk>/', DeletePriceView.as_view(), name='delete price'),
        path('details/<int:pk>/', DetailsPriceView.as_view(), name='details price'),
    ])),
    path('services/', DisplayAdditionalServicesView.as_view(), name='show additional services'),
    path('team/', AllEmployeeView.as_view(), name='team'),
    path('employer/', include([
        path('all/', AllCompanyView.as_view(), name='view all employer'),
        path('add/', CreateCompanyView.as_view(), name='add employer'),
        path('edit/<int:pk>/', EditCompanyView.as_view(), name='edit employer'),
        path('details/<int:pk>/', CompanyDetailView.as_view(), name='employer details'),
        path('delete/<int:pk>/', DeleteCompanyView.as_view(), name='delete employer'),
    ])),
)
