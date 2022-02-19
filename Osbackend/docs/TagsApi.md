# swagger_client.TagsApi

All URIs are relative to *https://api2.hiveos.farm/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**farms_farm_id_tags_delete**](TagsApi.md#farms_farm_id_tags_delete) | **DELETE** /farms/{farmId}/tags | Delete multiple tags
[**farms_farm_id_tags_get**](TagsApi.md#farms_farm_id_tags_get) | **GET** /farms/{farmId}/tags | Tags list
[**farms_farm_id_tags_multi_post**](TagsApi.md#farms_farm_id_tags_multi_post) | **POST** /farms/{farmId}/tags/multi | Create multiple tags
[**farms_farm_id_tags_patch**](TagsApi.md#farms_farm_id_tags_patch) | **PATCH** /farms/{farmId}/tags | Edit multiple tags
[**farms_farm_id_tags_post**](TagsApi.md#farms_farm_id_tags_post) | **POST** /farms/{farmId}/tags | Create new tag
[**farms_farm_id_tags_tag_id_delete**](TagsApi.md#farms_farm_id_tags_tag_id_delete) | **DELETE** /farms/{farmId}/tags/{tagId} | Delete tag
[**farms_farm_id_tags_tag_id_get**](TagsApi.md#farms_farm_id_tags_tag_id_get) | **GET** /farms/{farmId}/tags/{tagId} | Tag info
[**farms_farm_id_tags_tag_id_patch**](TagsApi.md#farms_farm_id_tags_tag_id_patch) | **PATCH** /farms/{farmId}/tags/{tagId} | Edit tag
[**tags_delete**](TagsApi.md#tags_delete) | **DELETE** /tags | Delete multiple tags
[**tags_get**](TagsApi.md#tags_get) | **GET** /tags | Tags list
[**tags_multi_post**](TagsApi.md#tags_multi_post) | **POST** /tags/multi | Create multiple tags
[**tags_patch**](TagsApi.md#tags_patch) | **PATCH** /tags | Edit multiple tags
[**tags_post**](TagsApi.md#tags_post) | **POST** /tags | Create new tag
[**tags_tag_id_delete**](TagsApi.md#tags_tag_id_delete) | **DELETE** /tags/{tagId} | Delete tag
[**tags_tag_id_get**](TagsApi.md#tags_tag_id_get) | **GET** /tags/{tagId} | Tag info
[**tags_tag_id_patch**](TagsApi.md#tags_tag_id_patch) | **PATCH** /tags/{tagId} | Edit tag


# **farms_farm_id_tags_delete**
> farms_farm_id_tags_delete(farm_id, body=body)

Delete multiple tags

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.IDs() # IDs |  (optional)

try:
    # Delete multiple tags
    api_instance.farms_farm_id_tags_delete(farm_id, body=body)
except ApiException as e:
    print("Exception when calling TagsApi->farms_farm_id_tags_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**IDs**](IDs.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_tags_get**
> object farms_farm_id_tags_get(farm_id)

Tags list

Returns tags that belong to given farm along with tags that belong to farm’s owner

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 

try:
    # Tags list
    api_response = api_instance.farms_farm_id_tags_get(farm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->farms_farm_id_tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_tags_multi_post**
> object farms_farm_id_tags_multi_post(farm_id, body=body)

Create multiple tags

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.Body() # Body |  (optional)

try:
    # Create multiple tags
    api_response = api_instance.farms_farm_id_tags_multi_post(farm_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->farms_farm_id_tags_multi_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**Body**](.md)|  | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_tags_patch**
> farms_farm_id_tags_patch(farm_id, body=body)

Edit multiple tags

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.Body() # Body |  (optional)

try:
    # Edit multiple tags
    api_instance.farms_farm_id_tags_patch(farm_id, body=body)
except ApiException as e:
    print("Exception when calling TagsApi->farms_farm_id_tags_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**Body**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_tags_post**
> TagF farms_farm_id_tags_post(farm_id, body=body)

Create new tag

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.TagCreateRequest() # TagCreateRequest |  (optional)

try:
    # Create new tag
    api_response = api_instance.farms_farm_id_tags_post(farm_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->farms_farm_id_tags_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**TagCreateRequest**](TagCreateRequest.md)|  | [optional] 

### Return type

[**TagF**](TagF.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_tags_tag_id_delete**
> farms_farm_id_tags_tag_id_delete(farm_id, tag_id)

Delete tag

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
tag_id = 56 # int | 

try:
    # Delete tag
    api_instance.farms_farm_id_tags_tag_id_delete(farm_id, tag_id)
except ApiException as e:
    print("Exception when calling TagsApi->farms_farm_id_tags_tag_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **tag_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_tags_tag_id_get**
> TagF farms_farm_id_tags_tag_id_get(farm_id, tag_id)

Tag info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
tag_id = 56 # int | 

try:
    # Tag info
    api_response = api_instance.farms_farm_id_tags_tag_id_get(farm_id, tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->farms_farm_id_tags_tag_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **tag_id** | **int**|  | 

### Return type

[**TagF**](TagF.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_tags_tag_id_patch**
> farms_farm_id_tags_tag_id_patch(farm_id, tag_id, body=body)

Edit tag

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
tag_id = 56 # int | 
body = swagger_client.TagUpdateRequest() # TagUpdateRequest |  (optional)

try:
    # Edit tag
    api_instance.farms_farm_id_tags_tag_id_patch(farm_id, tag_id, body=body)
except ApiException as e:
    print("Exception when calling TagsApi->farms_farm_id_tags_tag_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **tag_id** | **int**|  | 
 **body** | [**TagUpdateRequest**](TagUpdateRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_delete**
> tags_delete(body=body)

Delete multiple tags

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
body = swagger_client.IDs() # IDs |  (optional)

try:
    # Delete multiple tags
    api_instance.tags_delete(body=body)
except ApiException as e:
    print("Exception when calling TagsApi->tags_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IDs**](IDs.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_get**
> object tags_get(type_id=type_id)

Tags list

Returns tags that belong to current user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
type_id = 'type_id_example' # str | Return only records of these types, comma-separated list of IDs (optional)

try:
    # Tags list
    api_response = api_instance.tags_get(type_id=type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**| Return only records of these types, comma-separated list of IDs | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_multi_post**
> object tags_multi_post(body=body)

Create multiple tags

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body() # Body |  (optional)

try:
    # Create multiple tags
    api_response = api_instance.tags_multi_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->tags_multi_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](.md)|  | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_patch**
> tags_patch(body=body)

Edit multiple tags

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body() # Body |  (optional)

try:
    # Edit multiple tags
    api_instance.tags_patch(body=body)
except ApiException as e:
    print("Exception when calling TagsApi->tags_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_post**
> TagU tags_post(body=body)

Create new tag

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
body = swagger_client.TagUCreateRequest() # TagUCreateRequest |  (optional)

try:
    # Create new tag
    api_response = api_instance.tags_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->tags_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TagUCreateRequest**](TagUCreateRequest.md)|  | [optional] 

### Return type

[**TagU**](TagU.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_tag_id_delete**
> tags_tag_id_delete(tag_id)

Delete tag

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
tag_id = 56 # int | 

try:
    # Delete tag
    api_instance.tags_tag_id_delete(tag_id)
except ApiException as e:
    print("Exception when calling TagsApi->tags_tag_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_tag_id_get**
> TagU tags_tag_id_get(farm_id, tag_id)

Tag info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
tag_id = 56 # int | 

try:
    # Tag info
    api_response = api_instance.tags_tag_id_get(farm_id, tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->tags_tag_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **tag_id** | **int**|  | 

### Return type

[**TagU**](TagU.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_tag_id_patch**
> tags_tag_id_patch(tag_id, body=body)

Edit tag

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
tag_id = 56 # int | 
body = swagger_client.TagUUpdateRequest() # TagUUpdateRequest |  (optional)

try:
    # Edit tag
    api_instance.tags_tag_id_patch(tag_id, body=body)
except ApiException as e:
    print("Exception when calling TagsApi->tags_tag_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **int**|  | 
 **body** | [**TagUUpdateRequest**](TagUUpdateRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

