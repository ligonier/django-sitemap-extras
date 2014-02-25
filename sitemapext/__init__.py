try:
    from .views import (SitemapGenerator, SitemapIndex, SitemapView, VideoSitemapView, ImageSitemapView,
                        NewsSitemapView, MobileSitemapView, GoogleBotVerifierMixin)
except ImportError:
    pass


