# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    
"""

from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six

from douyin.open.video_poi.api_client import ApiClient


class PoiSearchApi(object):
    """NOTE: 由抖音小开自动生成，请勿自己修改
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def poi_search_keyword_get(self, access_token, count, keyword, **kwargs):
        """关键字搜索

        * Scope: `poi.search` 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poi_search_keyword_get(access_token, count, keyword, async_req=False)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: 调用/oauth/client_token/生成的token，此token不需要用户授权。 (required)
        :param int count: 每页数量 (required)
        :param str keyword: 查询关键字，例如美食 (required)
        :param int cursor: 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。
        :param str city: 查询城市，例如上海、北京
        :return: PoiSearchKeywordResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.poi_search_keyword_get_with_http_info(access_token, count, keyword, **kwargs)
        else:
            (data) = self.poi_search_keyword_get_with_http_info(access_token, count, keyword, **kwargs)
            return data

    def poi_search_keyword_get_with_http_info(self, access_token, count, keyword, **kwargs):
        """关键字搜索  # noqa: E501

        * Scope: `poi.search` 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poi_search_keyword_get_with_http_info(access_token, count, keyword, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str access_token: 调用/oauth/client_token/生成的token，此token不需要用户授权。 (required)
        :param int count: 每页数量 (required)
        :param str keyword: 查询关键字，例如美食 (required)
        :param int cursor: 分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。
        :param str city: 查询城市，例如上海、北京
        :return: PoiSearchKeywordResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'count', 'keyword', 'cursor', 'city']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method poi_search_keyword_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `poi_search_keyword_get`")
        # verify the required parameter 'count' is set
        if ('count' not in params or
                params['count'] is None):
            raise ValueError("Missing the required parameter `count` when calling `poi_search_keyword_get`")
        # verify the required parameter 'keyword' is set
        if ('keyword' not in params or
                params['keyword'] is None):
            raise ValueError("Missing the required parameter `keyword` when calling `poi_search_keyword_get`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))
        if 'count' in params:
            query_params.append(('count', params['count']))
        if 'keyword' in params:
            query_params.append(('keyword', params['keyword']))
        if 'city' in params:
            query_params.append(('city', params['city']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/poi/search/keyword/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PoiSearchKeywordResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
