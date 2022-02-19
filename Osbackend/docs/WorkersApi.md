# swagger_client.WorkersApi

All URIs are relative to *https://api2.hiveos.farm/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**farms_farm_id_workers_command_amd_upload_post**](WorkersApi.md#farms_farm_id_workers_command_amd_upload_post) | **POST** /farms/{farmId}/workers/command/amd_upload | Extended version of \&quot;amd_upload\&quot; command
[**farms_farm_id_workers_command_nvidia_upload_post**](WorkersApi.md#farms_farm_id_workers_command_nvidia_upload_post) | **POST** /farms/{farmId}/workers/command/nvidia_upload | Extended version of \&quot;nvidia_upload\&quot; command
[**farms_farm_id_workers_command_post**](WorkersApi.md#farms_farm_id_workers_command_post) | **POST** /farms/{farmId}/workers/command | Execute command on multiple workers
[**farms_farm_id_workers_delete**](WorkersApi.md#farms_farm_id_workers_delete) | **DELETE** /farms/{farmId}/workers | Delete multiple workers
[**farms_farm_id_workers_filters_get**](WorkersApi.md#farms_farm_id_workers_filters_get) | **GET** /farms/{farmId}/workers/filters | Available values for filters that are used in worker and GPU lists
[**farms_farm_id_workers_fix_auto_tags_post**](WorkersApi.md#farms_farm_id_workers_fix_auto_tags_post) | **POST** /farms/{farmId}/workers/fix_auto_tags | Synchronize auto-tags of all workers of the farm
[**farms_farm_id_workers_get**](WorkersApi.md#farms_farm_id_workers_get) | **GET** /farms/{farmId}/workers | Farm workers list
[**farms_farm_id_workers_gpus_get**](WorkersApi.md#farms_farm_id_workers_gpus_get) | **GET** /farms/{farmId}/workers/gpus | Farm workers GPUs list
[**farms_farm_id_workers_messages_delete**](WorkersApi.md#farms_farm_id_workers_messages_delete) | **DELETE** /farms/{farmId}/workers/messages | Delete all messages of all or provided workers
[**farms_farm_id_workers_messages_get**](WorkersApi.md#farms_farm_id_workers_messages_get) | **GET** /farms/{farmId}/workers/messages | Farm workers messages list
[**farms_farm_id_workers_multi_patch**](WorkersApi.md#farms_farm_id_workers_multi_patch) | **PATCH** /farms/{farmId}/workers/multi | Edit multiple workers
[**farms_farm_id_workers_multi_post**](WorkersApi.md#farms_farm_id_workers_multi_post) | **POST** /farms/{farmId}/workers/multi | Create multiple workers
[**farms_farm_id_workers_overclock_post**](WorkersApi.md#farms_farm_id_workers_overclock_post) | **POST** /farms/{farmId}/workers/overclock | Extended overclocking
[**farms_farm_id_workers_patch**](WorkersApi.md#farms_farm_id_workers_patch) | **PATCH** /farms/{farmId}/workers | Edit multiple workers at once
[**farms_farm_id_workers_post**](WorkersApi.md#farms_farm_id_workers_post) | **POST** /farms/{farmId}/workers | Create new worker
[**farms_farm_id_workers_preview_get**](WorkersApi.md#farms_farm_id_workers_preview_get) | **GET** /farms/{farmId}/workers/preview | Preview all workers of the farm
[**farms_farm_id_workers_reload_post**](WorkersApi.md#farms_farm_id_workers_reload_post) | **POST** /farms/{farmId}/workers/reload | Reload multiple workers
[**farms_farm_id_workers_transfer_post**](WorkersApi.md#farms_farm_id_workers_transfer_post) | **POST** /farms/{farmId}/workers/transfer | Transfer multiple workers to another farm
[**farms_farm_id_workers_worker_id_command_post**](WorkersApi.md#farms_farm_id_workers_worker_id_command_post) | **POST** /farms/{farmId}/workers/{workerId}/command | Execute command
[**farms_farm_id_workers_worker_id_configs_config_get**](WorkersApi.md#farms_farm_id_workers_worker_id_configs_config_get) | **GET** /farms/{farmId}/workers/{workerId}/configs/{config} | Get configuration file for worker
[**farms_farm_id_workers_worker_id_configs_get**](WorkersApi.md#farms_farm_id_workers_worker_id_configs_get) | **GET** /farms/{farmId}/workers/{workerId}/configs | Get configuration files for worker
[**farms_farm_id_workers_worker_id_delete**](WorkersApi.md#farms_farm_id_workers_worker_id_delete) | **DELETE** /farms/{farmId}/workers/{workerId} | Delete worker
[**farms_farm_id_workers_worker_id_fix_auto_tags_post**](WorkersApi.md#farms_farm_id_workers_worker_id_fix_auto_tags_post) | **POST** /farms/{farmId}/workers/{workerId}/fix_auto_tags | Synchronize auto-tags of the worker
[**farms_farm_id_workers_worker_id_get**](WorkersApi.md#farms_farm_id_workers_worker_id_get) | **GET** /farms/{farmId}/workers/{workerId} | Worker info
[**farms_farm_id_workers_worker_id_messages_delete**](WorkersApi.md#farms_farm_id_workers_worker_id_messages_delete) | **DELETE** /farms/{farmId}/workers/{workerId}/messages | Delete all worker messages
[**farms_farm_id_workers_worker_id_messages_get**](WorkersApi.md#farms_farm_id_workers_worker_id_messages_get) | **GET** /farms/{farmId}/workers/{workerId}/messages | Worker messages
[**farms_farm_id_workers_worker_id_messages_message_id_delete**](WorkersApi.md#farms_farm_id_workers_worker_id_messages_message_id_delete) | **DELETE** /farms/{farmId}/workers/{workerId}/messages/{messageId} | Delete message
[**farms_farm_id_workers_worker_id_messages_message_id_get**](WorkersApi.md#farms_farm_id_workers_worker_id_messages_message_id_get) | **GET** /farms/{farmId}/workers/{workerId}/messages/{messageId} | Get worker message
[**farms_farm_id_workers_worker_id_metrics_get**](WorkersApi.md#farms_farm_id_workers_worker_id_metrics_get) | **GET** /farms/{farmId}/workers/{workerId}/metrics | Worker metrics
[**farms_farm_id_workers_worker_id_password_put**](WorkersApi.md#farms_farm_id_workers_worker_id_password_put) | **PUT** /farms/{farmId}/workers/{workerId}/password | Update worker password
[**farms_farm_id_workers_worker_id_patch**](WorkersApi.md#farms_farm_id_workers_worker_id_patch) | **PATCH** /farms/{farmId}/workers/{workerId} | Edit worker
[**farms_farm_id_workers_worker_id_personal_settings_patch**](WorkersApi.md#farms_farm_id_workers_worker_id_personal_settings_patch) | **PATCH** /farms/{farmId}/workers/{workerId}/personal_settings | Update personal settings for the worker
[**farms_farm_id_workers_worker_id_reload_post**](WorkersApi.md#farms_farm_id_workers_worker_id_reload_post) | **POST** /farms/{farmId}/workers/{workerId}/reload | Reload worker
[**farms_farm_id_workers_worker_id_transfer_post**](WorkersApi.md#farms_farm_id_workers_worker_id_transfer_post) | **POST** /farms/{farmId}/workers/{workerId}/transfer | Transfer worker to another farm


# **farms_farm_id_workers_command_amd_upload_post**
> object farms_farm_id_workers_command_amd_upload_post(farm_id, body=body)

Extended version of \"amd_upload\" command

Allows to flash different AMD GPUs of different workers in one request.

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.Body() # Body |  (optional)

try:
    # Extended version of \"amd_upload\" command
    api_response = api_instance.farms_farm_id_workers_command_amd_upload_post(farm_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_command_amd_upload_post: %s\n" % e)
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

# **farms_farm_id_workers_command_nvidia_upload_post**
> object farms_farm_id_workers_command_nvidia_upload_post(farm_id, body=body)

Extended version of \"nvidia_upload\" command

Allows to flash different Nvidia GPUs of different workers in one request.

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.Body() # Body |  (optional)

try:
    # Extended version of \"nvidia_upload\" command
    api_response = api_instance.farms_farm_id_workers_command_nvidia_upload_post(farm_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_command_nvidia_upload_post: %s\n" % e)
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

# **farms_farm_id_workers_command_post**
> object farms_farm_id_workers_command_post(farm_id, body=body)

Execute command on multiple workers

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = NULL # object |  (optional)

try:
    # Execute command on multiple workers
    api_response = api_instance.farms_farm_id_workers_command_post(farm_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_command_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**object**](.md)|  | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_workers_delete**
> farms_farm_id_workers_delete(farm_id, body=body)

Delete multiple workers

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = NULL # object |  (optional)

try:
    # Delete multiple workers
    api_instance.farms_farm_id_workers_delete(farm_id, body=body)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**object**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_workers_filters_get**
> object farms_farm_id_workers_filters_get(farm_id)

Available values for filters that are used in worker and GPU lists

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 

try:
    # Available values for filters that are used in worker and GPU lists
    api_response = api_instance.farms_farm_id_workers_filters_get(farm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_filters_get: %s\n" % e)
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

# **farms_farm_id_workers_fix_auto_tags_post**
> farms_farm_id_workers_fix_auto_tags_post(farm_id)

Synchronize auto-tags of all workers of the farm

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 

try:
    # Synchronize auto-tags of all workers of the farm
    api_instance.farms_farm_id_workers_fix_auto_tags_post(farm_id)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_fix_auto_tags_post: %s\n" % e)
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

# **farms_farm_id_workers_get**
> object farms_farm_id_workers_get(farm_id, filter=filter, tags=tags, platform=platform)

Farm workers list

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
filter = 'filter_example' # str | Optional filter for workers (optional)
tags = 'tags_example' # str | Filter by tags. Comma-separated list of Tag IDs. (optional)
platform = 56 # int | Worker platform: * 1 - GPU * 2 - ASIC  (optional)

try:
    # Farm workers list
    api_response = api_instance.farms_farm_id_workers_get(farm_id, filter=filter, tags=tags, platform=platform)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **filter** | **str**| Optional filter for workers | [optional] 
 **tags** | **str**| Filter by tags. Comma-separated list of Tag IDs. | [optional] 
 **platform** | **int**| Worker platform: * 1 - GPU * 2 - ASIC  | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_workers_gpus_get**
> object farms_farm_id_workers_gpus_get(farm_id, worker_ids=worker_ids, tags=tags)

Farm workers GPUs list

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
worker_ids = 'worker_ids_example' # str | Return only records for these workers, comma-separated list of IDs (optional)
tags = 'tags_example' # str | Filter by tags. Comma-separated list of Tag IDs. (optional)

try:
    # Farm workers GPUs list
    api_response = api_instance.farms_farm_id_workers_gpus_get(farm_id, worker_ids=worker_ids, tags=tags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_gpus_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **worker_ids** | **str**| Return only records for these workers, comma-separated list of IDs | [optional] 
 **tags** | **str**| Filter by tags. Comma-separated list of Tag IDs. | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_workers_messages_delete**
> farms_farm_id_workers_messages_delete(farm_id, body=body)

Delete all messages of all or provided workers

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.Body() # Body |  (optional)

try:
    # Delete all messages of all or provided workers
    api_instance.farms_farm_id_workers_messages_delete(farm_id, body=body)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_messages_delete: %s\n" % e)
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

# **farms_farm_id_workers_messages_get**
> object farms_farm_id_workers_messages_get(farm_id, page=page, per_page=per_page, worker_ids=worker_ids, message_ids=message_ids, with_payload=with_payload, start_time=start_time)

Farm workers messages list

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
page = 1 # int | Page number (optional) (default to 1)
per_page = 56 # int | Per-page count (default is 15) (optional)
worker_ids = 'worker_ids_example' # str | Return only records for these workers, comma-separated list of IDs (optional)
message_ids = 'message_ids_example' # str | Return only these messages, comma-separated list of IDs (optional)
with_payload = 0 # int | Include message payload to ouput (optional) (default to 0)
start_time = 56 # int | Return only messages starting from given timestamp (optional)

try:
    # Farm workers messages list
    api_response = api_instance.farms_farm_id_workers_messages_get(farm_id, page=page, per_page=per_page, worker_ids=worker_ids, message_ids=message_ids, with_payload=with_payload, start_time=start_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_messages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Per-page count (default is 15) | [optional] 
 **worker_ids** | **str**| Return only records for these workers, comma-separated list of IDs | [optional] 
 **message_ids** | **str**| Return only these messages, comma-separated list of IDs | [optional] 
 **with_payload** | **int**| Include message payload to ouput | [optional] [default to 0]
 **start_time** | **int**| Return only messages starting from given timestamp | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_workers_multi_patch**
> object farms_farm_id_workers_multi_patch(farm_id, body=body)

Edit multiple workers

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.Body() # Body |  (optional)

try:
    # Edit multiple workers
    api_response = api_instance.farms_farm_id_workers_multi_patch(farm_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_multi_patch: %s\n" % e)
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

# **farms_farm_id_workers_multi_post**
> object farms_farm_id_workers_multi_post(farm_id, body=body)

Create multiple workers

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.Body() # Body |  (optional)

try:
    # Create multiple workers
    api_response = api_instance.farms_farm_id_workers_multi_post(farm_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_multi_post: %s\n" % e)
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

# **farms_farm_id_workers_overclock_post**
> object farms_farm_id_workers_overclock_post(farm_id, body=body)

Extended overclocking

Allows to overlock individual GPUs of different workers in one request. Provided configurations will be merged into actual overclock of corresponding worker. 

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.Body() # Body |  (optional)

try:
    # Extended overclocking
    api_response = api_instance.farms_farm_id_workers_overclock_post(farm_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_overclock_post: %s\n" % e)
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

# **farms_farm_id_workers_patch**
> object farms_farm_id_workers_patch(farm_id, merge=merge, body=body)

Edit multiple workers at once

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
merge = true # bool | Merge some fields instead of replace them. These fields are: * miners_config * watchdog * autofan * octofan * coolbox * fanflap * powermeter  (optional)
body = NULL # object |  (optional)

try:
    # Edit multiple workers at once
    api_response = api_instance.farms_farm_id_workers_patch(farm_id, merge=merge, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **merge** | **bool**| Merge some fields instead of replace them. These fields are: * miners_config * watchdog * autofan * octofan * coolbox * fanflap * powermeter  | [optional] 
 **body** | [**object**](.md)|  | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_workers_post**
> Worker farms_farm_id_workers_post(farm_id, body=body)

Create new worker

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.WorkerCreateRequest() # WorkerCreateRequest |  (optional)

try:
    # Create new worker
    api_response = api_instance.farms_farm_id_workers_post(farm_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**WorkerCreateRequest**](WorkerCreateRequest.md)|  | [optional] 

### Return type

[**Worker**](Worker.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_workers_preview_get**
> object farms_farm_id_workers_preview_get(farm_id, search_id=search_id)

Preview all workers of the farm

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
search_id = 'search_id_example' # str | ID of cached workers selection (optional)

try:
    # Preview all workers of the farm
    api_response = api_instance.farms_farm_id_workers_preview_get(farm_id, search_id=search_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_preview_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **search_id** | **str**| ID of cached workers selection | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_workers_reload_post**
> object farms_farm_id_workers_reload_post(farm_id, body=body)

Reload multiple workers

Send configuration to workers, including flight sheet and overclock

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = NULL # object |  (optional)

try:
    # Reload multiple workers
    api_response = api_instance.farms_farm_id_workers_reload_post(farm_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_reload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**object**](.md)|  | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_workers_transfer_post**
> farms_farm_id_workers_transfer_post(farm_id, body=body)

Transfer multiple workers to another farm

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = NULL # object |  (optional)

try:
    # Transfer multiple workers to another farm
    api_instance.farms_farm_id_workers_transfer_post(farm_id, body=body)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_transfer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**object**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_workers_worker_id_command_post**
> object farms_farm_id_workers_worker_id_command_post(farm_id, worker_id, body=body)

Execute command

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
worker_id = 56 # int | 
body = swagger_client.CommandRequest() # CommandRequest |  (optional)

try:
    # Execute command
    api_response = api_instance.farms_farm_id_workers_worker_id_command_post(farm_id, worker_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_worker_id_command_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **worker_id** | **int**|  | 
 **body** | [**CommandRequest**](CommandRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_workers_worker_id_configs_config_get**
> WorkerConfigFiles farms_farm_id_workers_worker_id_configs_config_get(farm_id, worker_id, config)

Get configuration file for worker

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
worker_id = 56 # int | 
config = 'config_example' # str | 

try:
    # Get configuration file for worker
    api_response = api_instance.farms_farm_id_workers_worker_id_configs_config_get(farm_id, worker_id, config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_worker_id_configs_config_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **worker_id** | **int**|  | 
 **config** | **str**|  | 

### Return type

[**WorkerConfigFiles**](WorkerConfigFiles.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_workers_worker_id_configs_get**
> WorkerConfigFiles farms_farm_id_workers_worker_id_configs_get(farm_id, worker_id)

Get configuration files for worker

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
worker_id = 56 # int | 

try:
    # Get configuration files for worker
    api_response = api_instance.farms_farm_id_workers_worker_id_configs_get(farm_id, worker_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_worker_id_configs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **worker_id** | **int**|  | 

### Return type

[**WorkerConfigFiles**](WorkerConfigFiles.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_workers_worker_id_delete**
> farms_farm_id_workers_worker_id_delete(farm_id, worker_id)

Delete worker

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
worker_id = 56 # int | 

try:
    # Delete worker
    api_instance.farms_farm_id_workers_worker_id_delete(farm_id, worker_id)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_worker_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **worker_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_workers_worker_id_fix_auto_tags_post**
> farms_farm_id_workers_worker_id_fix_auto_tags_post(farm_id, worker_id)

Synchronize auto-tags of the worker

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
worker_id = 56 # int | 

try:
    # Synchronize auto-tags of the worker
    api_instance.farms_farm_id_workers_worker_id_fix_auto_tags_post(farm_id, worker_id)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_worker_id_fix_auto_tags_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **worker_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_workers_worker_id_get**
> Worker farms_farm_id_workers_worker_id_get(farm_id, worker_id)

Worker info

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
worker_id = 56 # int | 

try:
    # Worker info
    api_response = api_instance.farms_farm_id_workers_worker_id_get(farm_id, worker_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_worker_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **worker_id** | **int**|  | 

### Return type

[**Worker**](Worker.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_workers_worker_id_messages_delete**
> farms_farm_id_workers_worker_id_messages_delete(farm_id, worker_id, body=body)

Delete all worker messages

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
worker_id = 56 # int | 
body = swagger_client.Body() # Body |  (optional)

try:
    # Delete all worker messages
    api_instance.farms_farm_id_workers_worker_id_messages_delete(farm_id, worker_id, body=body)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_worker_id_messages_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **worker_id** | **int**|  | 
 **body** | [**Body**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_workers_worker_id_messages_get**
> object farms_farm_id_workers_worker_id_messages_get(farm_id, worker_id, page=page, per_page=per_page, message_ids=message_ids, with_payload=with_payload, start_time=start_time)

Worker messages

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
worker_id = 56 # int | 
page = 1 # int | Page number (optional) (default to 1)
per_page = 56 # int | Per-page count (default is 15) (optional)
message_ids = 'message_ids_example' # str | Return only these messages, comma-separated list of IDs (optional)
with_payload = 0 # int | Include message payload to ouput (optional) (default to 0)
start_time = 56 # int | Return only messages starting from given timestamp (optional)

try:
    # Worker messages
    api_response = api_instance.farms_farm_id_workers_worker_id_messages_get(farm_id, worker_id, page=page, per_page=per_page, message_ids=message_ids, with_payload=with_payload, start_time=start_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_worker_id_messages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **worker_id** | **int**|  | 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Per-page count (default is 15) | [optional] 
 **message_ids** | **str**| Return only these messages, comma-separated list of IDs | [optional] 
 **with_payload** | **int**| Include message payload to ouput | [optional] [default to 0]
 **start_time** | **int**| Return only messages starting from given timestamp | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_workers_worker_id_messages_message_id_delete**
> farms_farm_id_workers_worker_id_messages_message_id_delete(farm_id, worker_id, message_id)

Delete message

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
worker_id = 56 # int | 
message_id = 56 # int | 

try:
    # Delete message
    api_instance.farms_farm_id_workers_worker_id_messages_message_id_delete(farm_id, worker_id, message_id)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_worker_id_messages_message_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **worker_id** | **int**|  | 
 **message_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_workers_worker_id_messages_message_id_get**
> WorkerMessageFull farms_farm_id_workers_worker_id_messages_message_id_get(farm_id, worker_id, message_id)

Get worker message

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
worker_id = 56 # int | 
message_id = 56 # int | 

try:
    # Get worker message
    api_response = api_instance.farms_farm_id_workers_worker_id_messages_message_id_get(farm_id, worker_id, message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_worker_id_messages_message_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **worker_id** | **int**|  | 
 **message_id** | **int**|  | 

### Return type

[**WorkerMessageFull**](WorkerMessageFull.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_workers_worker_id_metrics_get**
> object farms_farm_id_workers_worker_id_metrics_get(farm_id, worker_id, _date=_date, period=period, fill_gaps=fill_gaps)

Worker metrics

Provides metrics for current worker. Data is refreshed every 5 minutes. For 1 week period - metrics are downsampled by 15 minutes. For 1 month period - metrics are downsampled by 1 hour. 

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
worker_id = 56 # int | 
_date = 'today' # str | Start date (optional) (default to today)
period = '1d' # str | Period (1 day, 1 week, 1 month) (optional) (default to 1d)
fill_gaps = 0 # int | Fill gaps with empty points (optional) (default to 0)

try:
    # Worker metrics
    api_response = api_instance.farms_farm_id_workers_worker_id_metrics_get(farm_id, worker_id, _date=_date, period=period, fill_gaps=fill_gaps)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_worker_id_metrics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **worker_id** | **int**|  | 
 **_date** | **str**| Start date | [optional] [default to today]
 **period** | **str**| Period (1 day, 1 week, 1 month) | [optional] [default to 1d]
 **fill_gaps** | **int**| Fill gaps with empty points | [optional] [default to 0]

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_workers_worker_id_password_put**
> farms_farm_id_workers_worker_id_password_put(farm_id, worker_id, body=body)

Update worker password

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
worker_id = 56 # int | 
body = swagger_client.WorkerEditPassword() # WorkerEditPassword |  (optional)

try:
    # Update worker password
    api_instance.farms_farm_id_workers_worker_id_password_put(farm_id, worker_id, body=body)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_worker_id_password_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **worker_id** | **int**|  | 
 **body** | [**WorkerEditPassword**](WorkerEditPassword.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_workers_worker_id_patch**
> WorkerUpdatedResponse farms_farm_id_workers_worker_id_patch(farm_id, worker_id, body=body)

Edit worker

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
worker_id = 56 # int | 
body = swagger_client.WorkerEditRequest() # WorkerEditRequest |  (optional)

try:
    # Edit worker
    api_response = api_instance.farms_farm_id_workers_worker_id_patch(farm_id, worker_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_worker_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **worker_id** | **int**|  | 
 **body** | [**WorkerEditRequest**](WorkerEditRequest.md)|  | [optional] 

### Return type

[**WorkerUpdatedResponse**](WorkerUpdatedResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_workers_worker_id_personal_settings_patch**
> farms_farm_id_workers_worker_id_personal_settings_patch(farm_id, worker_id, body=body)

Update personal settings for the worker

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
worker_id = 56 # int | 
body = swagger_client.FarmPersonalSettings() # FarmPersonalSettings |  (optional)

try:
    # Update personal settings for the worker
    api_instance.farms_farm_id_workers_worker_id_personal_settings_patch(farm_id, worker_id, body=body)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_worker_id_personal_settings_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **worker_id** | **int**|  | 
 **body** | [**FarmPersonalSettings**](FarmPersonalSettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_workers_worker_id_reload_post**
> object farms_farm_id_workers_worker_id_reload_post(farm_id, worker_id)

Reload worker

Send configuration to worker, including flight sheet and overclock

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
worker_id = 56 # int | 

try:
    # Reload worker
    api_response = api_instance.farms_farm_id_workers_worker_id_reload_post(farm_id, worker_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_worker_id_reload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **worker_id** | **int**|  | 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_workers_worker_id_transfer_post**
> farms_farm_id_workers_worker_id_transfer_post(farm_id, worker_id, body=body)

Transfer worker to another farm

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
api_instance = swagger_client.WorkersApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
worker_id = 56 # int | 
body = swagger_client.WorkerTransferRequest() # WorkerTransferRequest |  (optional)

try:
    # Transfer worker to another farm
    api_instance.farms_farm_id_workers_worker_id_transfer_post(farm_id, worker_id, body=body)
except ApiException as e:
    print("Exception when calling WorkersApi->farms_farm_id_workers_worker_id_transfer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **worker_id** | **int**|  | 
 **body** | [**WorkerTransferRequest**](WorkerTransferRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

