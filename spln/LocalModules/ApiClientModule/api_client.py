#!/usr/bin/env python

import requests


class ApiClient(object):
    def __init__(self, baseURL, endpointURL, params):
        self.baseURL = baseURL
        self.endpointUrl = endpointURL
        self.params = params

    def _url(self, query):
        url = (self.baseURL + self.endpointUrl).format(str(query))
        print('URL: ' + url)
        return url

    def make_request(self, body=None):
        if self.params['method'] == 'GET':
            return requests.get(self._url(self.params['query']))

        if self.params['method'] == 'POST':
            return requests.get(self._url(self.params['query']), json=body)


def check_source(title):
    news_search_url = 'http://spnl-news-search.apphb.com/'
    news_search_endpoint = 'api/News/searchnews?query={:s}'

    params = {
        'method' : 'GET',
        'query' : title
    }

    response = ApiClient(news_search_url, news_search_endpoint, params).make_request()

    if response.status_code == 200:
        return response.json()
    else:
        return {}
