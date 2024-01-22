from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n"))
]
# urlpatterns.extend(
#     static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# )

# window
urlpatterns += [
    path("", include("window.urls")),
    path("", include("fleet.urls")),
]

# urlpatterns += [
#     # back store
#     path("store/<uuid:UUID>", include("backstore.urls")),
# ]
