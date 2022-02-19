# swagger_client.AclApi

All URIs are relative to *https://api2.hiveos.farm/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**farms_farm_id_acl_acl_id_delete**](AclApi.md#farms_farm_id_acl_acl_id_delete) | **DELETE** /farms/{farmId}/acl/{aclId} | Revoke farm privileges
[**farms_farm_id_acl_acl_id_get**](AclApi.md#farms_farm_id_acl_acl_id_get) | **GET** /farms/{farmId}/acl/{aclId} | Farm privileges for single user
[**farms_farm_id_acl_acl_id_patch**](AclApi.md#farms_farm_id_acl_acl_id_patch) | **PATCH** /farms/{farmId}/acl/{aclId} | Edit farm privileges
[**farms_farm_id_acl_delete**](AclApi.md#farms_farm_id_acl_delete) | **DELETE** /farms/{farmId}/acl | Revoke multiple privileges
[**farms_farm_id_acl_get**](AclApi.md#farms_farm_id_acl_get) | **GET** /farms/{farmId}/acl | Farm privileges
[**farms_farm_id_acl_me_delete**](AclApi.md#farms_farm_id_acl_me_delete) | **DELETE** /farms/{farmId}/acl/me | Remove my account from farm privileges
[**farms_farm_id_acl_post**](AclApi.md#farms_farm_id_acl_post) | **POST** /farms/{farmId}/acl | Grant farm privileges
[**farms_farm_id_acl_share_post**](AclApi.md#farms_farm_id_acl_share_post) | **POST** /farms/{farmId}/acl/share | Share access to farm for admins


# **farms_farm_id_acl_acl_id_delete**
> farms_farm_id_acl_acl_id_delete(farm_id, acl_id)

Revoke farm privileges

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
api_instance = swagger_client.AclApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
acl_id = 56 # int | 

try:
    # Revoke farm privileges
    api_instance.farms_farm_id_acl_acl_id_delete(farm_id, acl_id)
except ApiException as e:
    print("Exception when calling AclApi->farms_farm_id_acl_acl_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **acl_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_acl_acl_id_get**
> FarmAcl farms_farm_id_acl_acl_id_get(farm_id, acl_id)

Farm privileges for single user

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
api_instance = swagger_client.AclApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
acl_id = 56 # int | 

try:
    # Farm privileges for single user
    api_response = api_instance.farms_farm_id_acl_acl_id_get(farm_id, acl_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AclApi->farms_farm_id_acl_acl_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **acl_id** | **int**|  | 

### Return type

[**FarmAcl**](FarmAcl.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_acl_acl_id_patch**
> farms_farm_id_acl_acl_id_patch(farm_id, acl_id, body=body)

Edit farm privileges

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
api_instance = swagger_client.AclApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
acl_id = 56 # int | 
body = swagger_client.AclUpdateRequest() # AclUpdateRequest |  (optional)

try:
    # Edit farm privileges
    api_instance.farms_farm_id_acl_acl_id_patch(farm_id, acl_id, body=body)
except ApiException as e:
    print("Exception when calling AclApi->farms_farm_id_acl_acl_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **acl_id** | **int**|  | 
 **body** | [**AclUpdateRequest**](AclUpdateRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_acl_delete**
> farms_farm_id_acl_delete(farm_id, body=body)

Revoke multiple privileges

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
api_instance = swagger_client.AclApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.IDs() # IDs |  (optional)

try:
    # Revoke multiple privileges
    api_instance.farms_farm_id_acl_delete(farm_id, body=body)
except ApiException as e:
    print("Exception when calling AclApi->farms_farm_id_acl_delete: %s\n" % e)
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

# **farms_farm_id_acl_get**
> object farms_farm_id_acl_get(farm_id)

Farm privileges

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
api_instance = swagger_client.AclApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 

try:
    # Farm privileges
    api_response = api_instance.farms_farm_id_acl_get(farm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AclApi->farms_farm_id_acl_get: %s\n" % e)
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

# **farms_farm_id_acl_me_delete**
> farms_farm_id_acl_me_delete(farm_id)

Remove my account from farm privileges

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
api_instance = swagger_client.AclApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 

try:
    # Remove my account from farm privileges
    api_instance.farms_farm_id_acl_me_delete(farm_id)
except ApiException as e:
    print("Exception when calling AclApi->farms_farm_id_acl_me_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_acl_post**
> FarmAcl farms_farm_id_acl_post(farm_id, body=body)

Grant farm privileges

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
api_instance = swagger_client.AclApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.AclCreateRequest() # AclCreateRequest |  (optional)

try:
    # Grant farm privileges
    api_response = api_instance.farms_farm_id_acl_post(farm_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AclApi->farms_farm_id_acl_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**AclCreateRequest**](AclCreateRequest.md)|  | [optional] 

### Return type

[**FarmAcl**](FarmAcl.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_acl_share_post**
> FarmAcl farms_farm_id_acl_share_post(farm_id, body=body)

Share access to farm for admins

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
api_instance = swagger_client.AclApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.Body() # Body |  (optional)

try:
    # Share access to farm for admins
    api_response = api_instance.farms_farm_id_acl_share_post(farm_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AclApi->farms_farm_id_acl_share_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**Body**](.md)|  | [optional] 

### Return type

[**FarmAcl**](FarmAcl.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

