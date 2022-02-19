# swagger_client.KeysApi

All URIs are relative to *https://api2.hiveos.farm/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**farms_farm_id_keys_delete**](KeysApi.md#farms_farm_id_keys_delete) | **DELETE** /farms/{farmId}/keys | Delete multiple API keys
[**farms_farm_id_keys_get**](KeysApi.md#farms_farm_id_keys_get) | **GET** /farms/{farmId}/keys | Get list of attached API keys
[**farms_farm_id_keys_key_id_delete**](KeysApi.md#farms_farm_id_keys_key_id_delete) | **DELETE** /farms/{farmId}/keys/{keyId} | Detach API key
[**farms_farm_id_keys_key_id_get**](KeysApi.md#farms_farm_id_keys_key_id_get) | **GET** /farms/{farmId}/keys/{keyId} | Get attached API key info
[**farms_farm_id_keys_key_id_patch**](KeysApi.md#farms_farm_id_keys_key_id_patch) | **PATCH** /farms/{farmId}/keys/{keyId} | Edit attached API key
[**farms_farm_id_keys_post**](KeysApi.md#farms_farm_id_keys_post) | **POST** /farms/{farmId}/keys | Attach new API key
[**keys_delete**](KeysApi.md#keys_delete) | **DELETE** /keys | Delete multiple API keys
[**keys_get**](KeysApi.md#keys_get) | **GET** /keys | Get list of attached API keys
[**keys_key_id_delete**](KeysApi.md#keys_key_id_delete) | **DELETE** /keys/{keyId} | Detach API key
[**keys_key_id_get**](KeysApi.md#keys_key_id_get) | **GET** /keys/{keyId} | Get attached API key info
[**keys_key_id_patch**](KeysApi.md#keys_key_id_patch) | **PATCH** /keys/{keyId} | Edit attached API key
[**keys_post**](KeysApi.md#keys_post) | **POST** /keys | Attach new API key


# **farms_farm_id_keys_delete**
> farms_farm_id_keys_delete(farm_id, body=body)

Delete multiple API keys

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
api_instance = swagger_client.KeysApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.IDs() # IDs |  (optional)

try:
    # Delete multiple API keys
    api_instance.farms_farm_id_keys_delete(farm_id, body=body)
except ApiException as e:
    print("Exception when calling KeysApi->farms_farm_id_keys_delete: %s\n" % e)
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

# **farms_farm_id_keys_get**
> object farms_farm_id_keys_get(farm_id)

Get list of attached API keys

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
api_instance = swagger_client.KeysApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 

try:
    # Get list of attached API keys
    api_response = api_instance.farms_farm_id_keys_get(farm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeysApi->farms_farm_id_keys_get: %s\n" % e)
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

# **farms_farm_id_keys_key_id_delete**
> farms_farm_id_keys_key_id_delete(farm_id, key_id)

Detach API key

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
api_instance = swagger_client.KeysApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
key_id = 56 # int | 

try:
    # Detach API key
    api_instance.farms_farm_id_keys_key_id_delete(farm_id, key_id)
except ApiException as e:
    print("Exception when calling KeysApi->farms_farm_id_keys_key_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **key_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_keys_key_id_get**
> ApiKeyF farms_farm_id_keys_key_id_get(farm_id, key_id)

Get attached API key info

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
api_instance = swagger_client.KeysApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
key_id = 56 # int | 

try:
    # Get attached API key info
    api_response = api_instance.farms_farm_id_keys_key_id_get(farm_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeysApi->farms_farm_id_keys_key_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **key_id** | **int**|  | 

### Return type

[**ApiKeyF**](ApiKeyF.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_keys_key_id_patch**
> farms_farm_id_keys_key_id_patch(farm_id, key_id, body=body)

Edit attached API key

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
api_instance = swagger_client.KeysApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
key_id = 56 # int | 
body = swagger_client.ApiKeyUpdateRequest() # ApiKeyUpdateRequest |  (optional)

try:
    # Edit attached API key
    api_instance.farms_farm_id_keys_key_id_patch(farm_id, key_id, body=body)
except ApiException as e:
    print("Exception when calling KeysApi->farms_farm_id_keys_key_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **key_id** | **int**|  | 
 **body** | [**ApiKeyUpdateRequest**](ApiKeyUpdateRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_keys_post**
> ApiKeyF farms_farm_id_keys_post(farm_id, body=body)

Attach new API key

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
api_instance = swagger_client.KeysApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.ApiKeyCreateRequest() # ApiKeyCreateRequest |  (optional)

try:
    # Attach new API key
    api_response = api_instance.farms_farm_id_keys_post(farm_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeysApi->farms_farm_id_keys_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**ApiKeyCreateRequest**](ApiKeyCreateRequest.md)|  | [optional] 

### Return type

[**ApiKeyF**](ApiKeyF.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keys_delete**
> keys_delete(body=body)

Delete multiple API keys

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
api_instance = swagger_client.KeysApi(swagger_client.ApiClient(configuration))
body = swagger_client.IDs() # IDs |  (optional)

try:
    # Delete multiple API keys
    api_instance.keys_delete(body=body)
except ApiException as e:
    print("Exception when calling KeysApi->keys_delete: %s\n" % e)
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

# **keys_get**
> object keys_get()

Get list of attached API keys

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
api_instance = swagger_client.KeysApi(swagger_client.ApiClient(configuration))

try:
    # Get list of attached API keys
    api_response = api_instance.keys_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeysApi->keys_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keys_key_id_delete**
> keys_key_id_delete(key_id)

Detach API key

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
api_instance = swagger_client.KeysApi(swagger_client.ApiClient(configuration))
key_id = 56 # int | 

try:
    # Detach API key
    api_instance.keys_key_id_delete(key_id)
except ApiException as e:
    print("Exception when calling KeysApi->keys_key_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keys_key_id_get**
> ApiKeyU keys_key_id_get(key_id)

Get attached API key info

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
api_instance = swagger_client.KeysApi(swagger_client.ApiClient(configuration))
key_id = 56 # int | 

try:
    # Get attached API key info
    api_response = api_instance.keys_key_id_get(key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeysApi->keys_key_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **int**|  | 

### Return type

[**ApiKeyU**](ApiKeyU.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keys_key_id_patch**
> keys_key_id_patch(key_id, body=body)

Edit attached API key

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
api_instance = swagger_client.KeysApi(swagger_client.ApiClient(configuration))
key_id = 56 # int | 
body = swagger_client.ApiKeyUpdateRequest() # ApiKeyUpdateRequest |  (optional)

try:
    # Edit attached API key
    api_instance.keys_key_id_patch(key_id, body=body)
except ApiException as e:
    print("Exception when calling KeysApi->keys_key_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **int**|  | 
 **body** | [**ApiKeyUpdateRequest**](ApiKeyUpdateRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keys_post**
> ApiKeyU keys_post(body=body)

Attach new API key

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
api_instance = swagger_client.KeysApi(swagger_client.ApiClient(configuration))
body = swagger_client.ApiKeyCreateRequest() # ApiKeyCreateRequest |  (optional)

try:
    # Attach new API key
    api_response = api_instance.keys_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeysApi->keys_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiKeyCreateRequest**](ApiKeyCreateRequest.md)|  | [optional] 

### Return type

[**ApiKeyU**](ApiKeyU.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

