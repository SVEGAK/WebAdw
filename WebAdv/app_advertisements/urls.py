from .views import index, top_sellers,advertisement_post, login, profile, register
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', advertisement_post, name='adv-post'),
    path('login/', login, name='login'),
    path('profile/',  profile, name='profile'),
    path('register/',  register, name='register'),
    path('myauth/', include('app_auth.urls')),
    # path('advertisment/', advertisment, name='advertisment'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)