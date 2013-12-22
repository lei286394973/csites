from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pro2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'pro2.views.index', name='index'),
    url(r'^about_us', 'pro2.views.about_us', name='about_us'),
    url(r'^news_detail', 'pro2.views.news_detail', name='news_detail'),
    url(r'^news', 'pro2.views.news', name='news'),
    url(r'^message', 'pro2.views.message', name='message'),
    url(r'^product_detail', 'pro2.views.product_detail', name='product_detail'),
    url(r'^products', 'pro2.views.products', name='products'),
    url(r'^contact_us', 'pro2.views.contact_us', name='contact_us'),
)
