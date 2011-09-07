# -*- coding: utf-8 -*-
import gdata.youtube
import gdata.youtube.service
import gdata.alt.appengine
from ytlinker import settings

class YTLinkSearch(object):
    def __init__(self):
        self.client = gdata.youtube.service.YouTubeService()
        self.client.client_id = settings.YT_CLIENT_ID
        self.client.developer_key = settings.YT_DEV_KEY
        gdata.alt.appengine.run_on_appengine(self.client)
        pass
        
    def search(self, author, **kwargs):
        """Searches for videos assigned to the specified author
        @param kwargs: {
            "filter_string" : search filter string,
            "max_results" : max result count,
            "order_by" : sort order of results,
            "start_index" : start index of the search
        }
        @return yt feed object
        """
        query = gdata.youtube.service.YouTubeVideoQuery()
        query.author = author
        filter_string = kwargs.get('filter_string')
        if filter_string:
            query.vq = filter_string
        query.max_results = kwargs.get('max_results', 20)
        query.orderby = kwargs.get('order_by', 'published')
        start_index = kwargs.get('start_index')
        if start_index:
            query.start_index = start_index
        feed = self.client.YouTubeQuery(query)
        return feed
