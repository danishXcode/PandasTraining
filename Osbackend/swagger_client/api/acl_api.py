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


class AclApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def farms_farm_id_acl_acl_id_delete(self, farm_id, acl_id, **kwargs):  # noqa: E501
        """Revoke farm privileges  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_acl_acl_id_delete(farm_id, acl_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int farm_id: (required)
        :param int acl_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.farms_farm_id_acl_acl_id_delete_with_http_info(farm_id, acl_id, **kwargs)  # noqa: E501
        else:
            (data) = self.farms_farm_id_acl_acl_id_delete_with_http_info(farm_id, acl_id, **kwargs)  # noqa: E501
            return data

    def farms_farm_id_acl_acl_id_delete_with_http_info(self, farm_id, acl_id, **kwargs):  # noqa: E501
        """Revoke farm privileges  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_acl_acl_id_delete_with_http_info(farm_id, acl_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int farm_id: (required)
        :param int acl_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['farm_id', 'acl_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method farms_farm_id_acl_acl_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'farm_id' is set
        if self.api_client.client_side_validation and ('farm_id' not in params or
                                                       params['farm_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `farm_id` when calling `farms_farm_id_acl_acl_id_delete`")  # noqa: E501
        # verify the required parameter 'acl_id' is set
        if self.api_client.client_side_validation and ('acl_id' not in params or
                                                       params['acl_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `acl_id` when calling `farms_farm_id_acl_acl_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'farm_id' in params:
            path_params['farmId'] = params['farm_id']  # noqa: E501
        if 'acl_id' in params:
            path_params['aclId'] = params['acl_id']  # noqa: E501

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
            '/farms/{farmId}/acl/{aclId}', 'DELETE',
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

    def farms_farm_id_acl_acl_id_get(self, farm_id, acl_id, **kwargs):  # noqa: E501
        """Farm privileges for single user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_acl_acl_id_get(farm_id, acl_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int farm_id: (required)
        :param int acl_id: (required)
        :return: FarmAcl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.farms_farm_id_acl_acl_id_get_with_http_info(farm_id, acl_id, **kwargs)  # noqa: E501
        else:
            (data) = self.farms_farm_id_acl_acl_id_get_with_http_info(farm_id, acl_id, **kwargs)  # noqa: E501
            return data

    def farms_farm_id_acl_acl_id_get_with_http_info(self, farm_id, acl_id, **kwargs):  # noqa: E501
        """Farm privileges for single user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_acl_acl_id_get_with_http_info(farm_id, acl_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int farm_id: (required)
        :param int acl_id: (required)
        :return: FarmAcl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['farm_id', 'acl_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method farms_farm_id_acl_acl_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'farm_id' is set
        if self.api_client.client_side_validation and ('farm_id' not in params or
                                                       params['farm_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `farm_id` when calling `farms_farm_id_acl_acl_id_get`")  # noqa: E501
        # verify the required parameter 'acl_id' is set
        if self.api_client.client_side_validation and ('acl_id' not in params or
                                                       params['acl_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `acl_id` when calling `farms_farm_id_acl_acl_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'farm_id' in params:
            path_params['farmId'] = params['farm_id']  # noqa: E501
        if 'acl_id' in params:
            path_params['aclId'] = params['acl_id']  # noqa: E501

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
            '/farms/{farmId}/acl/{aclId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FarmAcl',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def farms_farm_id_acl_acl_id_patch(self, farm_id, acl_id, **kwargs):  # noqa: E501
        """Edit farm privileges  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_acl_acl_id_patch(farm_id, acl_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int farm_id: (required)
        :param int acl_id: (required)
        :param AclUpdateRequest body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.farms_farm_id_acl_acl_id_patch_with_http_info(farm_id, acl_id, **kwargs)  # noqa: E501
        else:
            (data) = self.farms_farm_id_acl_acl_id_patch_with_http_info(farm_id, acl_id, **kwargs)  # noqa: E501
            return data

    def farms_farm_id_acl_acl_id_patch_with_http_info(self, farm_id, acl_id, **kwargs):  # noqa: E501
        """Edit farm privileges  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_acl_acl_id_patch_with_http_info(farm_id, acl_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int farm_id: (required)
        :param int acl_id: (required)
        :param AclUpdateRequest body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['farm_id', 'acl_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method farms_farm_id_acl_acl_id_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'farm_id' is set
        if self.api_client.client_side_validation and ('farm_id' not in params or
                                                       params['farm_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `farm_id` when calling `farms_farm_id_acl_acl_id_patch`")  # noqa: E501
        # verify the required parameter 'acl_id' is set
        if self.api_client.client_side_validation and ('acl_id' not in params or
                                                       params['acl_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `acl_id` when calling `farms_farm_id_acl_acl_id_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'farm_id' in params:
            path_params['farmId'] = params['farm_id']  # noqa: E501
        if 'acl_id' in params:
            path_params['aclId'] = params['acl_id']  # noqa: E501

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
            '/farms/{farmId}/acl/{aclId}', 'PATCH',
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

    def farms_farm_id_acl_delete(self, farm_id, **kwargs):  # noqa: E501
        """Revoke multiple privileges  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_acl_delete(farm_id, async_req=True)
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
            return self.farms_farm_id_acl_delete_with_http_info(farm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.farms_farm_id_acl_delete_with_http_info(farm_id, **kwargs)  # noqa: E501
            return data

    def farms_farm_id_acl_delete_with_http_info(self, farm_id, **kwargs):  # noqa: E501
        """Revoke multiple privileges  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_acl_delete_with_http_info(farm_id, async_req=True)
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
                    " to method farms_farm_id_acl_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'farm_id' is set
        if self.api_client.client_side_validation and ('farm_id' not in params or
                                                       params['farm_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `farm_id` when calling `farms_farm_id_acl_delete`")  # noqa: E501

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
            '/farms/{farmId}/acl', 'DELETE',
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

    def farms_farm_id_acl_get(self, farm_id, **kwargs):  # noqa: E501
        """Farm privileges  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_acl_get(farm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int farm_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.farms_farm_id_acl_get_with_http_info(farm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.farms_farm_id_acl_get_with_http_info(farm_id, **kwargs)  # noqa: E501
            return data

    def farms_farm_id_acl_get_with_http_info(self, farm_id, **kwargs):  # noqa: E501
        """Farm privileges  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_acl_get_with_http_info(farm_id, async_req=True)
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
                    " to method farms_farm_id_acl_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'farm_id' is set
        if self.api_client.client_side_validation and ('farm_id' not in params or
                                                       params['farm_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `farm_id` when calling `farms_farm_id_acl_get`")  # noqa: E501

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
            '/farms/{farmId}/acl', 'GET',
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

    def farms_farm_id_acl_me_delete(self, farm_id, **kwargs):  # noqa: E501
        """Remove my account from farm privileges  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_acl_me_delete(farm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int farm_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.farms_farm_id_acl_me_delete_with_http_info(farm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.farms_farm_id_acl_me_delete_with_http_info(farm_id, **kwargs)  # noqa: E501
            return data

    def farms_farm_id_acl_me_delete_with_http_info(self, farm_id, **kwargs):  # noqa: E501
        """Remove my account from farm privileges  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_acl_me_delete_with_http_info(farm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int farm_id: (required)
        :return: None
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
                    " to method farms_farm_id_acl_me_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'farm_id' is set
        if self.api_client.client_side_validation and ('farm_id' not in params or
                                                       params['farm_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `farm_id` when calling `farms_farm_id_acl_me_delete`")  # noqa: E501

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
            '/farms/{farmId}/acl/me', 'DELETE',
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

    def farms_farm_id_acl_post(self, farm_id, **kwargs):  # noqa: E501
        """Grant farm privileges  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_acl_post(farm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int farm_id: (required)
        :param AclCreateRequest body:
        :return: FarmAcl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.farms_farm_id_acl_post_with_http_info(farm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.farms_farm_id_acl_post_with_http_info(farm_id, **kwargs)  # noqa: E501
            return data

    def farms_farm_id_acl_post_with_http_info(self, farm_id, **kwargs):  # noqa: E501
        """Grant farm privileges  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_acl_post_with_http_info(farm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int farm_id: (required)
        :param AclCreateRequest body:
        :return: FarmAcl
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
                    " to method farms_farm_id_acl_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'farm_id' is set
        if self.api_client.client_side_validation and ('farm_id' not in params or
                                                       params['farm_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `farm_id` when calling `farms_farm_id_acl_post`")  # noqa: E501

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
            '/farms/{farmId}/acl', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FarmAcl',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def farms_farm_id_acl_share_post(self, farm_id, **kwargs):  # noqa: E501
        """Share access to farm for admins  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_acl_share_post(farm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int farm_id: (required)
        :param Body body:
        :return: FarmAcl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.farms_farm_id_acl_share_post_with_http_info(farm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.farms_farm_id_acl_share_post_with_http_info(farm_id, **kwargs)  # noqa: E501
            return data

    def farms_farm_id_acl_share_post_with_http_info(self, farm_id, **kwargs):  # noqa: E501
        """Share access to farm for admins  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.farms_farm_id_acl_share_post_with_http_info(farm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int farm_id: (required)
        :param Body body:
        :return: FarmAcl
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
                    " to method farms_farm_id_acl_share_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'farm_id' is set
        if self.api_client.client_side_validation and ('farm_id' not in params or
                                                       params['farm_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `farm_id` when calling `farms_farm_id_acl_share_post`")  # noqa: E501

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
            '/farms/{farmId}/acl/share', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FarmAcl',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
