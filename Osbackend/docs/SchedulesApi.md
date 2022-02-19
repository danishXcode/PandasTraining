# swagger_client.SchedulesApi

All URIs are relative to *https://api2.hiveos.farm/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**farms_farm_id_schedules_delete**](SchedulesApi.md#farms_farm_id_schedules_delete) | **DELETE** /farms/{farmId}/schedules | Delete multiple Schedules
[**farms_farm_id_schedules_get**](SchedulesApi.md#farms_farm_id_schedules_get) | **GET** /farms/{farmId}/schedules | Schedules list
[**farms_farm_id_schedules_post**](SchedulesApi.md#farms_farm_id_schedules_post) | **POST** /farms/{farmId}/schedules | Create new Schedule
[**farms_farm_id_schedules_schedule_id_delete**](SchedulesApi.md#farms_farm_id_schedules_schedule_id_delete) | **DELETE** /farms/{farmId}/schedules/{scheduleId} | Delete Schedule
[**farms_farm_id_schedules_schedule_id_get**](SchedulesApi.md#farms_farm_id_schedules_schedule_id_get) | **GET** /farms/{farmId}/schedules/{scheduleId} | Get Schedule
[**farms_farm_id_schedules_schedule_id_patch**](SchedulesApi.md#farms_farm_id_schedules_schedule_id_patch) | **PATCH** /farms/{farmId}/schedules/{scheduleId} | Edit Schedule
[**schedules_delete**](SchedulesApi.md#schedules_delete) | **DELETE** /schedules | Delete multiple Schedules
[**schedules_get**](SchedulesApi.md#schedules_get) | **GET** /schedules | Schedules list
[**schedules_post**](SchedulesApi.md#schedules_post) | **POST** /schedules | Create new Schedule
[**schedules_schedule_id_delete**](SchedulesApi.md#schedules_schedule_id_delete) | **DELETE** /schedules/{scheduleId} | Delete Schedule
[**schedules_schedule_id_get**](SchedulesApi.md#schedules_schedule_id_get) | **GET** /schedules/{scheduleId} | Get Schedule
[**schedules_schedule_id_patch**](SchedulesApi.md#schedules_schedule_id_patch) | **PATCH** /schedules/{scheduleId} | Edit Schedule


# **farms_farm_id_schedules_delete**
> farms_farm_id_schedules_delete(farm_id, body=body)

Delete multiple Schedules

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
api_instance = swagger_client.SchedulesApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.IDs() # IDs |  (optional)

try:
    # Delete multiple Schedules
    api_instance.farms_farm_id_schedules_delete(farm_id, body=body)
except ApiException as e:
    print("Exception when calling SchedulesApi->farms_farm_id_schedules_delete: %s\n" % e)
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

# **farms_farm_id_schedules_get**
> object farms_farm_id_schedules_get(farm_id, performed=performed, planned=planned, action=action, command=command, tag_ids=tag_ids)

Schedules list

Returns Schedules that belong to given farm

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
api_instance = swagger_client.SchedulesApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
performed = true # bool | Get only performed schedules (optional)
planned = true # bool | Get only planned schedules (optional)
action = 'action_example' # str | Get schedules with next actions. Supported multiple comma-separated actions (optional)
command = 'command_example' # str | Get schedules with next commands. Supported multiple comma-separated values (optional)
tag_ids = 'tag_ids_example' # str | Return only records for these tags, comma-separated list of IDs (optional)

try:
    # Schedules list
    api_response = api_instance.farms_farm_id_schedules_get(farm_id, performed=performed, planned=planned, action=action, command=command, tag_ids=tag_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulesApi->farms_farm_id_schedules_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **performed** | **bool**| Get only performed schedules | [optional] 
 **planned** | **bool**| Get only planned schedules | [optional] 
 **action** | **str**| Get schedules with next actions. Supported multiple comma-separated actions | [optional] 
 **command** | **str**| Get schedules with next commands. Supported multiple comma-separated values | [optional] 
 **tag_ids** | **str**| Return only records for these tags, comma-separated list of IDs | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_schedules_post**
> ScheduleF farms_farm_id_schedules_post(farm_id, body=body)

Create new Schedule

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
api_instance = swagger_client.SchedulesApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.ScheduleCreateUpdateRequestF() # ScheduleCreateUpdateRequestF |  (optional)

try:
    # Create new Schedule
    api_response = api_instance.farms_farm_id_schedules_post(farm_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulesApi->farms_farm_id_schedules_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**ScheduleCreateUpdateRequestF**](ScheduleCreateUpdateRequestF.md)|  | [optional] 

### Return type

[**ScheduleF**](ScheduleF.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_schedules_schedule_id_delete**
> farms_farm_id_schedules_schedule_id_delete(farm_id, schedule_id)

Delete Schedule

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
api_instance = swagger_client.SchedulesApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
schedule_id = 56 # int | 

try:
    # Delete Schedule
    api_instance.farms_farm_id_schedules_schedule_id_delete(farm_id, schedule_id)
except ApiException as e:
    print("Exception when calling SchedulesApi->farms_farm_id_schedules_schedule_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **schedule_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_schedules_schedule_id_get**
> ScheduleF farms_farm_id_schedules_schedule_id_get(farm_id, schedule_id)

Get Schedule

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
api_instance = swagger_client.SchedulesApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
schedule_id = 56 # int | 

try:
    # Get Schedule
    api_response = api_instance.farms_farm_id_schedules_schedule_id_get(farm_id, schedule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulesApi->farms_farm_id_schedules_schedule_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **schedule_id** | **int**|  | 

### Return type

[**ScheduleF**](ScheduleF.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_schedules_schedule_id_patch**
> farms_farm_id_schedules_schedule_id_patch(farm_id, schedule_id, body=body)

Edit Schedule

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
api_instance = swagger_client.SchedulesApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
schedule_id = 56 # int | 
body = swagger_client.ScheduleCreateUpdateRequestF() # ScheduleCreateUpdateRequestF |  (optional)

try:
    # Edit Schedule
    api_instance.farms_farm_id_schedules_schedule_id_patch(farm_id, schedule_id, body=body)
except ApiException as e:
    print("Exception when calling SchedulesApi->farms_farm_id_schedules_schedule_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **schedule_id** | **int**|  | 
 **body** | [**ScheduleCreateUpdateRequestF**](ScheduleCreateUpdateRequestF.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_delete**
> schedules_delete(body=body)

Delete multiple Schedules

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
api_instance = swagger_client.SchedulesApi(swagger_client.ApiClient(configuration))
body = swagger_client.IDs() # IDs |  (optional)

try:
    # Delete multiple Schedules
    api_instance.schedules_delete(body=body)
except ApiException as e:
    print("Exception when calling SchedulesApi->schedules_delete: %s\n" % e)
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

# **schedules_get**
> object schedules_get()

Schedules list

Returns Schedules that belong to current user

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
api_instance = swagger_client.SchedulesApi(swagger_client.ApiClient(configuration))

try:
    # Schedules list
    api_response = api_instance.schedules_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulesApi->schedules_get: %s\n" % e)
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

# **schedules_post**
> ScheduleU schedules_post(body=body)

Create new Schedule

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
api_instance = swagger_client.SchedulesApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScheduleCreateUpdateRequestU() # ScheduleCreateUpdateRequestU |  (optional)

try:
    # Create new Schedule
    api_response = api_instance.schedules_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulesApi->schedules_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScheduleCreateUpdateRequestU**](ScheduleCreateUpdateRequestU.md)|  | [optional] 

### Return type

[**ScheduleU**](ScheduleU.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_id_delete**
> schedules_schedule_id_delete(schedule_id)

Delete Schedule

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
api_instance = swagger_client.SchedulesApi(swagger_client.ApiClient(configuration))
schedule_id = 56 # int | 

try:
    # Delete Schedule
    api_instance.schedules_schedule_id_delete(schedule_id)
except ApiException as e:
    print("Exception when calling SchedulesApi->schedules_schedule_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_id_get**
> ScheduleU schedules_schedule_id_get(schedule_id)

Get Schedule

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
api_instance = swagger_client.SchedulesApi(swagger_client.ApiClient(configuration))
schedule_id = 56 # int | 

try:
    # Get Schedule
    api_response = api_instance.schedules_schedule_id_get(schedule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulesApi->schedules_schedule_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_id** | **int**|  | 

### Return type

[**ScheduleU**](ScheduleU.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedules_schedule_id_patch**
> schedules_schedule_id_patch(schedule_id, body=body)

Edit Schedule

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
api_instance = swagger_client.SchedulesApi(swagger_client.ApiClient(configuration))
schedule_id = 56 # int | 
body = swagger_client.ScheduleCreateUpdateRequestU() # ScheduleCreateUpdateRequestU |  (optional)

try:
    # Edit Schedule
    api_instance.schedules_schedule_id_patch(schedule_id, body=body)
except ApiException as e:
    print("Exception when calling SchedulesApi->schedules_schedule_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_id** | **int**|  | 
 **body** | [**ScheduleCreateUpdateRequestU**](ScheduleCreateUpdateRequestU.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

