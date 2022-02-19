# swagger_client.FsApi

All URIs are relative to *https://api2.hiveos.farm/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**farms_farm_id_fs_delete**](FsApi.md#farms_farm_id_fs_delete) | **DELETE** /farms/{farmId}/fs | Delete multiple flight sheets
[**farms_farm_id_fs_fs_id_delete**](FsApi.md#farms_farm_id_fs_fs_id_delete) | **DELETE** /farms/{farmId}/fs/{fsId} | Delete flight sheet
[**farms_farm_id_fs_fs_id_get**](FsApi.md#farms_farm_id_fs_fs_id_get) | **GET** /farms/{farmId}/fs/{fsId} | Flight sheet info
[**farms_farm_id_fs_fs_id_patch**](FsApi.md#farms_farm_id_fs_fs_id_patch) | **PATCH** /farms/{farmId}/fs/{fsId} | Edit flight sheet
[**farms_farm_id_fs_get**](FsApi.md#farms_farm_id_fs_get) | **GET** /farms/{farmId}/fs | Flight sheets list
[**farms_farm_id_fs_post**](FsApi.md#farms_farm_id_fs_post) | **POST** /farms/{farmId}/fs | Create new flight sheet
[**fs_delete**](FsApi.md#fs_delete) | **DELETE** /fs | Delete multiple flight sheets
[**fs_fs_id_delete**](FsApi.md#fs_fs_id_delete) | **DELETE** /fs/{fsId} | Delete flight sheet
[**fs_fs_id_get**](FsApi.md#fs_fs_id_get) | **GET** /fs/{fsId} | Flight sheet info
[**fs_fs_id_patch**](FsApi.md#fs_fs_id_patch) | **PATCH** /fs/{fsId} | Edit flight sheet
[**fs_get**](FsApi.md#fs_get) | **GET** /fs | Flight sheets list
[**fs_post**](FsApi.md#fs_post) | **POST** /fs | Create new flight sheet


# **farms_farm_id_fs_delete**
> farms_farm_id_fs_delete(farm_id, body=body)

Delete multiple flight sheets

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
api_instance = swagger_client.FsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.IDs() # IDs |  (optional)

try:
    # Delete multiple flight sheets
    api_instance.farms_farm_id_fs_delete(farm_id, body=body)
except ApiException as e:
    print("Exception when calling FsApi->farms_farm_id_fs_delete: %s\n" % e)
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

# **farms_farm_id_fs_fs_id_delete**
> farms_farm_id_fs_fs_id_delete(farm_id, fs_id)

Delete flight sheet

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
api_instance = swagger_client.FsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
fs_id = 56 # int | 

try:
    # Delete flight sheet
    api_instance.farms_farm_id_fs_fs_id_delete(farm_id, fs_id)
except ApiException as e:
    print("Exception when calling FsApi->farms_farm_id_fs_fs_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **fs_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_fs_fs_id_get**
> FlightSheetF farms_farm_id_fs_fs_id_get(farm_id, fs_id)

Flight sheet info

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
api_instance = swagger_client.FsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
fs_id = 56 # int | 

try:
    # Flight sheet info
    api_response = api_instance.farms_farm_id_fs_fs_id_get(farm_id, fs_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsApi->farms_farm_id_fs_fs_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **fs_id** | **int**|  | 

### Return type

[**FlightSheetF**](FlightSheetF.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_fs_fs_id_patch**
> farms_farm_id_fs_fs_id_patch(farm_id, fs_id, body=body)

Edit flight sheet

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
api_instance = swagger_client.FsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
fs_id = 56 # int | 
body = swagger_client.FSUpdateRequest() # FSUpdateRequest |  (optional)

try:
    # Edit flight sheet
    api_instance.farms_farm_id_fs_fs_id_patch(farm_id, fs_id, body=body)
except ApiException as e:
    print("Exception when calling FsApi->farms_farm_id_fs_fs_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **fs_id** | **int**|  | 
 **body** | [**FSUpdateRequest**](FSUpdateRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_fs_get**
> object farms_farm_id_fs_get(farm_id)

Flight sheets list

Returns flight sheets that belong to given farm along with flight sheets that belong to farm's owner

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
api_instance = swagger_client.FsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 

try:
    # Flight sheets list
    api_response = api_instance.farms_farm_id_fs_get(farm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsApi->farms_farm_id_fs_get: %s\n" % e)
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

# **farms_farm_id_fs_post**
> FlightSheetF farms_farm_id_fs_post(farm_id, body=body)

Create new flight sheet

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
api_instance = swagger_client.FsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.FSCreateRequest() # FSCreateRequest |  (optional)

try:
    # Create new flight sheet
    api_response = api_instance.farms_farm_id_fs_post(farm_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsApi->farms_farm_id_fs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**FSCreateRequest**](FSCreateRequest.md)|  | [optional] 

### Return type

[**FlightSheetF**](FlightSheetF.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fs_delete**
> fs_delete(farm_id, body=body)

Delete multiple flight sheets

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
api_instance = swagger_client.FsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.IDs() # IDs |  (optional)

try:
    # Delete multiple flight sheets
    api_instance.fs_delete(farm_id, body=body)
except ApiException as e:
    print("Exception when calling FsApi->fs_delete: %s\n" % e)
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

# **fs_fs_id_delete**
> fs_fs_id_delete(farm_id, fs_id)

Delete flight sheet

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
api_instance = swagger_client.FsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
fs_id = 56 # int | 

try:
    # Delete flight sheet
    api_instance.fs_fs_id_delete(farm_id, fs_id)
except ApiException as e:
    print("Exception when calling FsApi->fs_fs_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **fs_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fs_fs_id_get**
> FlightSheetU fs_fs_id_get(farm_id, fs_id)

Flight sheet info

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
api_instance = swagger_client.FsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
fs_id = 56 # int | 

try:
    # Flight sheet info
    api_response = api_instance.fs_fs_id_get(farm_id, fs_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsApi->fs_fs_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **fs_id** | **int**|  | 

### Return type

[**FlightSheetU**](FlightSheetU.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fs_fs_id_patch**
> fs_fs_id_patch(farm_id, fs_id, body=body)

Edit flight sheet

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
api_instance = swagger_client.FsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
fs_id = 56 # int | 
body = swagger_client.FSUpdateRequest() # FSUpdateRequest |  (optional)

try:
    # Edit flight sheet
    api_instance.fs_fs_id_patch(farm_id, fs_id, body=body)
except ApiException as e:
    print("Exception when calling FsApi->fs_fs_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **fs_id** | **int**|  | 
 **body** | [**FSUpdateRequest**](FSUpdateRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fs_get**
> object fs_get(farm_id)

Flight sheets list

Returns flight sheets that belong to current user

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
api_instance = swagger_client.FsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 

try:
    # Flight sheets list
    api_response = api_instance.fs_get(farm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsApi->fs_get: %s\n" % e)
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

# **fs_post**
> FlightSheetU fs_post(farm_id, body=body)

Create new flight sheet

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
api_instance = swagger_client.FsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.FSCreateRequest() # FSCreateRequest |  (optional)

try:
    # Create new flight sheet
    api_response = api_instance.fs_post(farm_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsApi->fs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**FSCreateRequest**](FSCreateRequest.md)|  | [optional] 

### Return type

[**FlightSheetU**](FlightSheetU.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

