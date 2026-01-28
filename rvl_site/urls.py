from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from main import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("lang/<str:lang>/", views.home, name="home_lang"),
    path("about/", views.about, name="about"),
    path("about/<str:lang>/", views.about, name="about_lang"),
    path("structure/", views.structure, name="structure"),
    path("structure/<str:lang>/", views.structure, name="structure_lang"),
    path("services/", views.services, name="services"),
    path("services/<str:lang>/", views.services, name="services_lang"),
    path("documents/", views.documents, name="documents"),
    path("documents/<str:lang>/", views.documents, name="documents_lang"),
    path("training/", views.training, name="training"),
    path("training/<str:lang>/", views.training, name="training_lang"),
    path("legal/", views.legal, name="legal"),
    path("legal/<str:lang>/", views.legal, name="legal_lang"),
    path("news/", views.news, name="news"),
    path("news/<str:lang>/", views.news, name="news_lang"),
    path("proposals/", views.proposals, name="proposals"),
    path("proposals/<str:lang>/", views.proposals, name="proposals_lang"),
    path("quality/", views.quality, name="quality"),
    path("quality/<str:lang>/", views.quality, name="quality_lang"),
    path("careers/", views.careers, name="careers"),
    path("careers/<str:lang>/", views.careers, name="careers_lang"),
    path("faq/", views.faq, name="faq"),
    path("faq/<str:lang>/", views.faq, name="faq_lang"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/<str:lang>/", views.dashboard, name="dashboard_lang"),
    path("contacts/", views.contacts, name="contacts"),
    path("contacts/<str:lang>/", views.contacts, name="contacts_lang"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
