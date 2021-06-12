# api.py

# from wagtail.api.v2.endpoints import PagesAPIEndpoint
from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.images.api.v2.views import ImagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet
from django.urls import path, reverse


class MyPagesAPIEndpoint(PagesAPIViewSet):
    """
    Our custom Pages API endpoint that allows finding pages by pk or slug
    """

    def detail_view(self, request, pk=None, slug=None):
        param = pk
        if slug is not None:
            self.lookup_field = 'slug'
            param = slug
        return super().detail_view(request, param)

    @classmethod
    def get_urlpatterns(cls):
        """
        This returns a list of URL patterns for the endpoint
        """
        return [
            path('', cls.as_view({'get': 'listing_view'}), name='listing'),
            path('<int:pk>/', cls.as_view({'get': 'detail_view'}), name='detail'),
            path('<slug:slug>/', cls.as_view({'get': 'detail_view'}), name='detail'),
            path('find/', cls.as_view({'get': 'find_view'}), name='find'),
        ]


# Create the router. "wagtailapi" is the URL namespace
api_router = WagtailAPIRouter('wagtailapi')

# Add the three endpoints using the "register_endpoint" method.
# The first parameter is the name of the endpoint (eg. pages, images). This
# is used in the URL of the endpoint
# The second parameter is the endpoint class that handles the requests
api_router.register_endpoint('pages', MyPagesAPIEndpoint)
api_router.register_endpoint('images', ImagesAPIViewSet)
api_router.register_endpoint('documents', DocumentsAPIViewSet)