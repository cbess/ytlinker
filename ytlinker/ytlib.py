import gdata.youtube
import gdata.youtube.service
import gdata.alt.appengine


class YTLinkSearch(object):
    def __init__(self):
        self.client = gdata.youtube.service.YouTubeService()
        pass
        
    def search(self, author, **kwargs):
        """Searches for videos assigned to the specified author
        @param kwargs: {
            "filter_string" : search filter string
        }
        @return yt feed object
        """
        query = gdata.youtube.service.YouTubeVideoQuery()
        query.author = author
        query.vq = kwargs.get('filter_string', '')
        query.max_results = kwargs.get('max_results', 20)
        query.orderby = kwargs.get('order_by', 'relevance')
        feed = self.client.YouTubeQuery(query)
        return feed

