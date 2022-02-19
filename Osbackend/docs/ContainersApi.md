# swagger_client.ContainersApi

All URIs are relative to *https://api2.hiveos.farm/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**farms_farm_id_containers_container_id_delete**](ContainersApi.md#farms_farm_id_containers_container_id_delete) | **DELETE** /farms/{farmId}/containers/{containerId} | Delete container
[**farms_farm_id_containers_container_id_get**](ContainersApi.md#farms_farm_id_containers_container_id_get) | **GET** /farms/{farmId}/containers/{containerId} | Container info
[**farms_farm_id_containers_container_id_patch**](ContainersApi.md#farms_farm_id_containers_container_id_patch) | **PATCH** /farms/{farmId}/containers/{containerId} | Edit container
[**farms_farm_id_containers_delete**](ContainersApi.md#farms_farm_id_containers_delete) | **DELETE** /farms/{farmId}/containers | Delete multiple containers
[**farms_farm_id_containers_get**](ContainersApi.md#farms_farm_id_containers_get) | **GET** /farms/{farmId}/containers | Farm containers list
[**farms_farm_id_containers_post**](ContainersApi.md#farms_farm_id_containers_post) | **POST** /farms/{farmId}/containers | Create new container


# **farms_farm_id_containers_container_id_delete**
> farms_farm_id_containers_container_id_delete(farm_id, container_id)

Delete container

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
api_instance = swagger_client.ContainersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
container_id = 56 # int | 

try:
    # Delete container
    api_instance.farms_farm_id_containers_container_id_delete(farm_id, container_id)
except ApiException as e:
    print("Exception when calling ContainersApi->farms_farm_id_containers_container_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **container_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_containers_container_id_get**
> Container farms_farm_id_containers_container_id_get(farm_id, container_id)

Container info

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
api_instance = swagger_client.ContainersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
container_id = 56 # int | 

try:
    # Container info
    api_response = api_instance.farms_farm_id_containers_container_id_get(farm_id, container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->farms_farm_id_containers_container_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **container_id** | **int**|  | 

### Return type

[**Container**](Container.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_containers_container_id_patch**
> farms_farm_id_containers_container_id_patch(farm_id, container_id, body=body)

Edit container

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
api_instance = swagger_client.ContainersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
container_id = 56 # int | 
body = swagger_client.ContainerUpdateRequest() # ContainerUpdateRequest |  (optional)

try:
    # Edit container
    api_instance.farms_farm_id_containers_container_id_patch(farm_id, container_id, body=body)
except ApiException as e:
    print("Exception when calling ContainersApi->farms_farm_id_containers_container_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **container_id** | **int**|  | 
 **body** | [**ContainerUpdateRequest**](ContainerUpdateRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_containers_delete**
> farms_farm_id_containers_delete(farm_id, body=body)

Delete multiple containers

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
api_instance = swagger_client.ContainersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.IDs() # IDs |  (optional)

try:
    # Delete multiple containers
    api_instance.farms_farm_id_containers_delete(farm_id, body=body)
except ApiException as e:
    print("Exception when calling ContainersApi->farms_farm_id_containers_delete: %s\n" % e)
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

# **farms_farm_id_containers_get**
> object farms_farm_id_containers_get(farm_id)

Farm containers list

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
api_instance = swagger_client.ContainersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 

try:
    # Farm containers list
    api_response = api_instance.farms_farm_id_containers_get(farm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->farms_farm_id_containers_get: %s\n" % e)
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

# **farms_farm_id_containers_post**
> Container farms_farm_id_containers_post(farm_id, body=body)

Create new container

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
api_instance = swagger_client.ContainersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.ContainerCreateRequest() # ContainerCreateRequest |  (optional)

try:
    # Create new container
    api_response = api_instance.farms_farm_id_containers_post(farm_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->farms_farm_id_containers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**ContainerCreateRequest**](ContainerCreateRequest.md)|  | [optional] 

### Return type

[**Container**](Container.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

