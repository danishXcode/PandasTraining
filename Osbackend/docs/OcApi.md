# swagger_client.OcApi

All URIs are relative to *https://api2.hiveos.farm/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**farms_farm_id_oc_delete**](OcApi.md#farms_farm_id_oc_delete) | **DELETE** /farms/{farmId}/oc | Delete multiple OC profiles
[**farms_farm_id_oc_get**](OcApi.md#farms_farm_id_oc_get) | **GET** /farms/{farmId}/oc | Farm OC list
[**farms_farm_id_oc_oc_id_delete**](OcApi.md#farms_farm_id_oc_oc_id_delete) | **DELETE** /farms/{farmId}/oc/{ocId} | Delete OC
[**farms_farm_id_oc_oc_id_get**](OcApi.md#farms_farm_id_oc_oc_id_get) | **GET** /farms/{farmId}/oc/{ocId} | OC info
[**farms_farm_id_oc_oc_id_patch**](OcApi.md#farms_farm_id_oc_oc_id_patch) | **PATCH** /farms/{farmId}/oc/{ocId} | Edit OC
[**farms_farm_id_oc_post**](OcApi.md#farms_farm_id_oc_post) | **POST** /farms/{farmId}/oc | Create new OC
[**oc_delete**](OcApi.md#oc_delete) | **DELETE** /oc | Delete multiple OC profiles
[**oc_get**](OcApi.md#oc_get) | **GET** /oc | OC list
[**oc_oc_id_delete**](OcApi.md#oc_oc_id_delete) | **DELETE** /oc/{ocId} | Delete OC
[**oc_oc_id_get**](OcApi.md#oc_oc_id_get) | **GET** /oc/{ocId} | OC info
[**oc_oc_id_patch**](OcApi.md#oc_oc_id_patch) | **PATCH** /oc/{ocId} | Edit OC
[**oc_post**](OcApi.md#oc_post) | **POST** /oc | Create new OC


# **farms_farm_id_oc_delete**
> farms_farm_id_oc_delete(farm_id, body=body)

Delete multiple OC profiles

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
api_instance = swagger_client.OcApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.IDs() # IDs |  (optional)

try:
    # Delete multiple OC profiles
    api_instance.farms_farm_id_oc_delete(farm_id, body=body)
except ApiException as e:
    print("Exception when calling OcApi->farms_farm_id_oc_delete: %s\n" % e)
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

# **farms_farm_id_oc_get**
> object farms_farm_id_oc_get(farm_id)

Farm OC list

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
api_instance = swagger_client.OcApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 

try:
    # Farm OC list
    api_response = api_instance.farms_farm_id_oc_get(farm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OcApi->farms_farm_id_oc_get: %s\n" % e)
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

# **farms_farm_id_oc_oc_id_delete**
> farms_farm_id_oc_oc_id_delete(farm_id, oc_id)

Delete OC

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
api_instance = swagger_client.OcApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
oc_id = 56 # int | 

try:
    # Delete OC
    api_instance.farms_farm_id_oc_oc_id_delete(farm_id, oc_id)
except ApiException as e:
    print("Exception when calling OcApi->farms_farm_id_oc_oc_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **oc_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_oc_oc_id_get**
> OCF farms_farm_id_oc_oc_id_get(farm_id, oc_id)

OC info

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
api_instance = swagger_client.OcApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
oc_id = 56 # int | 

try:
    # OC info
    api_response = api_instance.farms_farm_id_oc_oc_id_get(farm_id, oc_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OcApi->farms_farm_id_oc_oc_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **oc_id** | **int**|  | 

### Return type

[**OCF**](OCF.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_oc_oc_id_patch**
> farms_farm_id_oc_oc_id_patch(farm_id, oc_id, body=body)

Edit OC

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
api_instance = swagger_client.OcApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
oc_id = 56 # int | 
body = swagger_client.OCUpdateRequest() # OCUpdateRequest |  (optional)

try:
    # Edit OC
    api_instance.farms_farm_id_oc_oc_id_patch(farm_id, oc_id, body=body)
except ApiException as e:
    print("Exception when calling OcApi->farms_farm_id_oc_oc_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **oc_id** | **int**|  | 
 **body** | [**OCUpdateRequest**](OCUpdateRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_oc_post**
> OCF farms_farm_id_oc_post(farm_id, body=body)

Create new OC

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
api_instance = swagger_client.OcApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.OCCreateRequest() # OCCreateRequest |  (optional)

try:
    # Create new OC
    api_response = api_instance.farms_farm_id_oc_post(farm_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OcApi->farms_farm_id_oc_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**OCCreateRequest**](OCCreateRequest.md)|  | [optional] 

### Return type

[**OCF**](OCF.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oc_delete**
> oc_delete(body=body)

Delete multiple OC profiles

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
api_instance = swagger_client.OcApi(swagger_client.ApiClient(configuration))
body = swagger_client.IDs() # IDs |  (optional)

try:
    # Delete multiple OC profiles
    api_instance.oc_delete(body=body)
except ApiException as e:
    print("Exception when calling OcApi->oc_delete: %s\n" % e)
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

# **oc_get**
> object oc_get()

OC list

Returns overclocking profiles that belong to current user

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
api_instance = swagger_client.OcApi(swagger_client.ApiClient(configuration))

try:
    # OC list
    api_response = api_instance.oc_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OcApi->oc_get: %s\n" % e)
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

# **oc_oc_id_delete**
> oc_oc_id_delete(oc_id)

Delete OC

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
api_instance = swagger_client.OcApi(swagger_client.ApiClient(configuration))
oc_id = 56 # int | 

try:
    # Delete OC
    api_instance.oc_oc_id_delete(oc_id)
except ApiException as e:
    print("Exception when calling OcApi->oc_oc_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oc_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oc_oc_id_get**
> OCU oc_oc_id_get(oc_id)

OC info

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
api_instance = swagger_client.OcApi(swagger_client.ApiClient(configuration))
oc_id = 56 # int | 

try:
    # OC info
    api_response = api_instance.oc_oc_id_get(oc_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OcApi->oc_oc_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oc_id** | **int**|  | 

### Return type

[**OCU**](OCU.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oc_oc_id_patch**
> oc_oc_id_patch(oc_id, body=body)

Edit OC

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
api_instance = swagger_client.OcApi(swagger_client.ApiClient(configuration))
oc_id = 56 # int | 
body = swagger_client.OCUpdateRequest() # OCUpdateRequest |  (optional)

try:
    # Edit OC
    api_instance.oc_oc_id_patch(oc_id, body=body)
except ApiException as e:
    print("Exception when calling OcApi->oc_oc_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oc_id** | **int**|  | 
 **body** | [**OCUpdateRequest**](OCUpdateRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oc_post**
> OCU oc_post(body=body)

Create new OC

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
api_instance = swagger_client.OcApi(swagger_client.ApiClient(configuration))
body = swagger_client.OCCreateRequest() # OCCreateRequest |  (optional)

try:
    # Create new OC
    api_response = api_instance.oc_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OcApi->oc_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OCCreateRequest**](OCCreateRequest.md)|  | [optional] 

### Return type

[**OCU**](OCU.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

