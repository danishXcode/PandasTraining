# swagger_client.RomsApi

All URIs are relative to *https://api2.hiveos.farm/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**farms_farm_id_roms_delete**](RomsApi.md#farms_farm_id_roms_delete) | **DELETE** /farms/{farmId}/roms | Delete multiple ROMs
[**farms_farm_id_roms_get**](RomsApi.md#farms_farm_id_roms_get) | **GET** /farms/{farmId}/roms | ROMs list
[**farms_farm_id_roms_post**](RomsApi.md#farms_farm_id_roms_post) | **POST** /farms/{farmId}/roms | Create new ROM
[**farms_farm_id_roms_rom_id_delete**](RomsApi.md#farms_farm_id_roms_rom_id_delete) | **DELETE** /farms/{farmId}/roms/{romId} | Delete ROM
[**farms_farm_id_roms_rom_id_get**](RomsApi.md#farms_farm_id_roms_rom_id_get) | **GET** /farms/{farmId}/roms/{romId} | Get ROM with contents
[**farms_farm_id_roms_rom_id_patch**](RomsApi.md#farms_farm_id_roms_rom_id_patch) | **PATCH** /farms/{farmId}/roms/{romId} | Edit ROM
[**roms_delete**](RomsApi.md#roms_delete) | **DELETE** /roms | Delete multiple ROMs
[**roms_get**](RomsApi.md#roms_get) | **GET** /roms | ROMs list
[**roms_post**](RomsApi.md#roms_post) | **POST** /roms | Create new ROM
[**roms_rom_id_delete**](RomsApi.md#roms_rom_id_delete) | **DELETE** /roms/{romId} | Delete ROM
[**roms_rom_id_get**](RomsApi.md#roms_rom_id_get) | **GET** /roms/{romId} | Get ROM with contents
[**roms_rom_id_patch**](RomsApi.md#roms_rom_id_patch) | **PATCH** /roms/{romId} | Edit ROM


# **farms_farm_id_roms_delete**
> farms_farm_id_roms_delete(farm_id, body=body)

Delete multiple ROMs

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
api_instance = swagger_client.RomsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.IDs() # IDs |  (optional)

try:
    # Delete multiple ROMs
    api_instance.farms_farm_id_roms_delete(farm_id, body=body)
except ApiException as e:
    print("Exception when calling RomsApi->farms_farm_id_roms_delete: %s\n" % e)
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

# **farms_farm_id_roms_get**
> object farms_farm_id_roms_get(farm_id)

ROMs list

Returns ROMs that belong to given farm along with ROMs that belong to farm's owner

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
api_instance = swagger_client.RomsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 

try:
    # ROMs list
    api_response = api_instance.farms_farm_id_roms_get(farm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RomsApi->farms_farm_id_roms_get: %s\n" % e)
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

# **farms_farm_id_roms_post**
> RomListItemF farms_farm_id_roms_post(farm_id, body=body)

Create new ROM

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
api_instance = swagger_client.RomsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.RomCreateUpdateRequest() # RomCreateUpdateRequest |  (optional)

try:
    # Create new ROM
    api_response = api_instance.farms_farm_id_roms_post(farm_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RomsApi->farms_farm_id_roms_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**RomCreateUpdateRequest**](RomCreateUpdateRequest.md)|  | [optional] 

### Return type

[**RomListItemF**](RomListItemF.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_roms_rom_id_delete**
> farms_farm_id_roms_rom_id_delete(farm_id, rom_id)

Delete ROM

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
api_instance = swagger_client.RomsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
rom_id = 56 # int | 

try:
    # Delete ROM
    api_instance.farms_farm_id_roms_rom_id_delete(farm_id, rom_id)
except ApiException as e:
    print("Exception when calling RomsApi->farms_farm_id_roms_rom_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **rom_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_roms_rom_id_get**
> RomF farms_farm_id_roms_rom_id_get(farm_id, rom_id)

Get ROM with contents

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
api_instance = swagger_client.RomsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
rom_id = 56 # int | 

try:
    # Get ROM with contents
    api_response = api_instance.farms_farm_id_roms_rom_id_get(farm_id, rom_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RomsApi->farms_farm_id_roms_rom_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **rom_id** | **int**|  | 

### Return type

[**RomF**](RomF.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_roms_rom_id_patch**
> farms_farm_id_roms_rom_id_patch(farm_id, rom_id, body=body)

Edit ROM

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
api_instance = swagger_client.RomsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
rom_id = 56 # int | 
body = swagger_client.RomCreateUpdateRequest() # RomCreateUpdateRequest |  (optional)

try:
    # Edit ROM
    api_instance.farms_farm_id_roms_rom_id_patch(farm_id, rom_id, body=body)
except ApiException as e:
    print("Exception when calling RomsApi->farms_farm_id_roms_rom_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **rom_id** | **int**|  | 
 **body** | [**RomCreateUpdateRequest**](RomCreateUpdateRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roms_delete**
> roms_delete(body=body)

Delete multiple ROMs

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
api_instance = swagger_client.RomsApi(swagger_client.ApiClient(configuration))
body = swagger_client.IDs() # IDs |  (optional)

try:
    # Delete multiple ROMs
    api_instance.roms_delete(body=body)
except ApiException as e:
    print("Exception when calling RomsApi->roms_delete: %s\n" % e)
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

# **roms_get**
> object roms_get()

ROMs list

Returns ROMs that belong to current user

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
api_instance = swagger_client.RomsApi(swagger_client.ApiClient(configuration))

try:
    # ROMs list
    api_response = api_instance.roms_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RomsApi->roms_get: %s\n" % e)
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

# **roms_post**
> RomListItemU roms_post(body=body)

Create new ROM

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
api_instance = swagger_client.RomsApi(swagger_client.ApiClient(configuration))
body = swagger_client.RomCreateUpdateRequest() # RomCreateUpdateRequest |  (optional)

try:
    # Create new ROM
    api_response = api_instance.roms_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RomsApi->roms_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RomCreateUpdateRequest**](RomCreateUpdateRequest.md)|  | [optional] 

### Return type

[**RomListItemU**](RomListItemU.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roms_rom_id_delete**
> roms_rom_id_delete(rom_id)

Delete ROM

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
api_instance = swagger_client.RomsApi(swagger_client.ApiClient(configuration))
rom_id = 56 # int | 

try:
    # Delete ROM
    api_instance.roms_rom_id_delete(rom_id)
except ApiException as e:
    print("Exception when calling RomsApi->roms_rom_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rom_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roms_rom_id_get**
> RomU roms_rom_id_get(rom_id)

Get ROM with contents

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
api_instance = swagger_client.RomsApi(swagger_client.ApiClient(configuration))
rom_id = 56 # int | 

try:
    # Get ROM with contents
    api_response = api_instance.roms_rom_id_get(rom_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RomsApi->roms_rom_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rom_id** | **int**|  | 

### Return type

[**RomU**](RomU.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roms_rom_id_patch**
> roms_rom_id_patch(rom_id, body=body)

Edit ROM

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
api_instance = swagger_client.RomsApi(swagger_client.ApiClient(configuration))
rom_id = 56 # int | 
body = swagger_client.RomCreateUpdateRequest() # RomCreateUpdateRequest |  (optional)

try:
    # Edit ROM
    api_instance.roms_rom_id_patch(rom_id, body=body)
except ApiException as e:
    print("Exception when calling RomsApi->roms_rom_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rom_id** | **int**|  | 
 **body** | [**RomCreateUpdateRequest**](RomCreateUpdateRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

