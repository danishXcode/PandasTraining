# coding: utf-8

"""
    Hive OS API

    App API for Hive OS 2.0  # noqa: E501

    OpenAPI spec version: 2.1-beta
    Contact: brain@hiveos.farm
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ContainersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def farms_farm_id_containers_container_id_delete(self, farm_id, container_id, **kwargs):  # noqa: E501
        """Delete container  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_containers_container_id_delete(farm_id, container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int farm_id: (required)
        :param int container_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.farms_farm_id_containers_container_id_delete_with_http_info(farm_id, container_id, **kwargs)  # noqa: E501
        else:
            (data) = self.farms_farm_id_containers_container_id_delete_with_http_info(farm_id, container_id, **kwargs)  # noqa: E501
            return data

    def farms_farm_id_containers_container_id_delete_with_http_info(self, farm_id, container_id, **kwargs):  # noqa: E501
        """Delete container  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_containers_container_id_delete_with_http_info(farm_id, container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int farm_id: (required)
        :param int container_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['farm_id', 'container_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method farms_farm_id_containers_container_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'farm_id' is set
        if self.api_client.client_side_validation and ('farm_id' not in params or
                                                       params['farm_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `farm_id` when calling `farms_farm_id_containers_container_id_delete`")  # noqa: E501
        # verify the required parameter 'container_id' is set
        if self.api_client.client_side_validation and ('container_id' not in params or
                                                       params['container_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `container_id` when calling `farms_farm_id_containers_container_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'farm_id' in params:
            path_params['farmId'] = params['farm_id']  # noqa: E501
        if 'container_id' in params:
            path_params['containerId'] = params['container_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/farms/{farmId}/containers/{containerId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def farms_farm_id_containers_container_id_get(self, farm_id, container_id, **kwargs):  # noqa: E501
        """Container info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_containers_container_id_get(farm_id, container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int farm_id: (required)
        :param int container_id: (required)
        :return: Container
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.farms_farm_id_containers_container_id_get_with_http_info(farm_id, container_id, **kwargs)  # noqa: E501
        else:
            (data) = self.farms_farm_id_containers_container_id_get_with_http_info(farm_id, container_id, **kwargs)  # noqa: E501
            return data

    def farms_farm_id_containers_container_id_get_with_http_info(self, farm_id, container_id, **kwargs):  # noqa: E501
        """Container info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_containers_container_id_get_with_http_info(farm_id, container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int farm_id: (required)
        :param int container_id: (required)
        :return: Container
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['farm_id', 'container_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method farms_farm_id_containers_container_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'farm_id' is set
        if self.api_client.client_side_validation and ('farm_id' not in params or
                                                       params['farm_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `farm_id` when calling `farms_farm_id_containers_container_id_get`")  # noqa: E501
        # verify the required parameter 'container_id' is set
        if self.api_client.client_side_validation and ('container_id' not in params or
                                                       params['container_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `container_id` when calling `farms_farm_id_containers_container_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'farm_id' in params:
            path_params['farmId'] = params['farm_id']  # noqa: E501
        if 'container_id' in params:
            path_params['containerId'] = params['container_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/farms/{farmId}/containers/{containerId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Container',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def farms_farm_id_containers_container_id_patch(self, farm_id, container_id, **kwargs):  # noqa: E501
        """Edit container  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_containers_container_id_patch(farm_id, container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int farm_id: (required)
        :param int container_id: (required)
        :param ContainerUpdateRequest body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.farms_farm_id_containers_container_id_patch_with_http_info(farm_id, container_id, **kwargs)  # noqa: E501
        else:
            (data) = self.farms_farm_id_containers_container_id_patch_with_http_info(farm_id, container_id, **kwargs)  # noqa: E501
            return data

    def farms_farm_id_containers_container_id_patch_with_http_info(self, farm_id, container_id, **kwargs):  # noqa: E501
        """Edit container  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_containers_container_id_patch_with_http_info(farm_id, container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int farm_id: (required)
        :param int container_id: (required)
        :param ContainerUpdateRequest body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['farm_id', 'container_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method farms_farm_id_containers_container_id_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'farm_id' is set
        if self.api_client.client_side_validation and ('farm_id' not in params or
                                                       params['farm_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `farm_id` when calling `farms_farm_id_containers_container_id_patch`")  # noqa: E501
        # verify the required parameter 'container_id' is set
        if self.api_client.client_side_validation and ('container_id' not in params or
                                                       params['container_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `container_id` when calling `farms_farm_id_containers_container_id_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'farm_id' in params:
            path_params['farmId'] = params['farm_id']  # noqa: E501
        if 'container_id' in params:
            path_params['containerId'] = params['container_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/farms/{farmId}/containers/{containerId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def farms_farm_id_containers_delete(self, farm_id, **kwargs):  # noqa: E501
        """Delete multiple containers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_containers_delete(farm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int farm_id: (required)
        :param IDs body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.farms_farm_id_containers_delete_with_http_info(farm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.farms_farm_id_containers_delete_with_http_info(farm_id, **kwargs)  # noqa: E501
            return data

    def farms_farm_id_containers_delete_with_http_info(self, farm_id, **kwargs):  # noqa: E501
        """Delete multiple containers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_containers_delete_with_http_info(farm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int farm_id: (required)
        :param IDs body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['farm_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method farms_farm_id_containers_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'farm_id' is set
        if self.api_client.client_side_validation and ('farm_id' not in params or
                                                       params['farm_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `farm_id` when calling `farms_farm_id_containers_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'farm_id' in params:
            path_params['farmId'] = params['farm_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/farms/{farmId}/containers', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def farms_farm_id_containers_get(self, farm_id, **kwargs):  # noqa: E501
        """Farm containers list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_containers_get(farm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int farm_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.farms_farm_id_containers_get_with_http_info(farm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.farms_farm_id_containers_get_with_http_info(farm_id, **kwargs)  # noqa: E501
            return data

    def farms_farm_id_containers_get_with_http_info(self, farm_id, **kwargs):  # noqa: E501
        """Farm containers list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_containers_get_with_http_info(farm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int farm_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['farm_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method farms_farm_id_containers_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'farm_id' is set
        if self.api_client.client_side_validation and ('farm_id' not in params or
                                                       params['farm_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `farm_id` when calling `farms_farm_id_containers_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'farm_id' in params:
            path_params['farmId'] = params['farm_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/farms/{farmId}/containers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def farms_farm_id_containers_post(self, farm_id, **kwargs):  # noqa: E501
        """Create new container  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_containers_post(farm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int farm_id: (required)
        :param ContainerCreateRequest body:
        :return: Container
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.farms_farm_id_containers_post_with_http_info(farm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.farms_farm_id_containers_post_with_http_info(farm_id, **kwargs)  # noqa: E501
            return data

    def farms_farm_id_containers_post_with_http_info(self, farm_id, **kwargs):  # noqa: E501
        """Create new container  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_containers_post_with_http_info(farm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int farm_id: (required)
        :param ContainerCreateRequest body:
        :return: Container
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['farm_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method farms_farm_id_containers_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'farm_id' is set
        if self.api_client.client_side_validation and ('farm_id' not in params or
                                                       params['farm_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `farm_id` when calling `farms_farm_id_containers_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'farm_id' in params:
            path_params['farmId'] = params['farm_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/farms/{farmId}/containers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Container',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
