# swagger_client.FarmsApi

All URIs are relative to *https://api2.hiveos.farm/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**farms_delete**](FarmsApi.md#farms_delete) | **DELETE** /farms | Delete multiple farms
[**farms_farm_id_configs_config_get**](FarmsApi.md#farms_farm_id_configs_config_get) | **GET** /farms/{farmId}/configs/{config} | Get configuration file for farm
[**farms_farm_id_configs_get**](FarmsApi.md#farms_farm_id_configs_get) | **GET** /farms/{farmId}/configs | Get configuration files for farm
[**farms_farm_id_delete**](FarmsApi.md#farms_farm_id_delete) | **DELETE** /farms/{farmId} | Delete farm
[**farms_farm_id_deposit_address_get**](FarmsApi.md#farms_farm_id_deposit_address_get) | **GET** /farms/{farmId}/deposit/address | Get list of generated payment addresses
[**farms_farm_id_deposit_address_post**](FarmsApi.md#farms_farm_id_deposit_address_post) | **POST** /farms/{farmId}/deposit/address | Generate payment address for deposits
[**farms_farm_id_deposit_post**](FarmsApi.md#farms_farm_id_deposit_post) | **POST** /farms/{farmId}/deposit | Make deposit to the farm from account balance
[**farms_farm_id_events_get**](FarmsApi.md#farms_farm_id_events_get) | **GET** /farms/{farmId}/events | Farm events
[**farms_farm_id_get**](FarmsApi.md#farms_farm_id_get) | **GET** /farms/{farmId} | Farm info
[**farms_farm_id_invoice_get**](FarmsApi.md#farms_farm_id_invoice_get) | **GET** /farms/{farmId}/invoice | Generate invoice for specified period
[**farms_farm_id_metrics_get**](FarmsApi.md#farms_farm_id_metrics_get) | **GET** /farms/{farmId}/metrics | Farm metrics
[**farms_farm_id_notifications_get**](FarmsApi.md#farms_farm_id_notifications_get) | **GET** /farms/{farmId}/notifications | Get notifications settings
[**farms_farm_id_notifications_patch**](FarmsApi.md#farms_farm_id_notifications_patch) | **PATCH** /farms/{farmId}/notifications | Update notifications settings
[**farms_farm_id_patch**](FarmsApi.md#farms_farm_id_patch) | **PATCH** /farms/{farmId} | Edit farm
[**farms_farm_id_payer_delete**](FarmsApi.md#farms_farm_id_payer_delete) | **DELETE** /farms/{farmId}/payer | Unassign farm payer and restore default value
[**farms_farm_id_personal_settings_patch**](FarmsApi.md#farms_farm_id_personal_settings_patch) | **PATCH** /farms/{farmId}/personal_settings | Update personal settings for the farm
[**farms_farm_id_power_report_get**](FarmsApi.md#farms_farm_id_power_report_get) | **GET** /farms/{farmId}/power_report | Generate report about power consumption for specified period
[**farms_farm_id_send_money_post**](FarmsApi.md#farms_farm_id_send_money_post) | **POST** /farms/{farmId}/send_money | Send money to user
[**farms_farm_id_stats_get**](FarmsApi.md#farms_farm_id_stats_get) | **GET** /farms/{farmId}/stats | Farm stats
[**farms_farm_id_transactions_get**](FarmsApi.md#farms_farm_id_transactions_get) | **GET** /farms/{farmId}/transactions | Transactions history
[**farms_farm_id_transfer_delete**](FarmsApi.md#farms_farm_id_transfer_delete) | **DELETE** /farms/{farmId}/transfer | Cancel farm transfer request
[**farms_farm_id_transfer_get**](FarmsApi.md#farms_farm_id_transfer_get) | **GET** /farms/{farmId}/transfer | Get active farm transfer request
[**farms_farm_id_transfer_post**](FarmsApi.md#farms_farm_id_transfer_post) | **POST** /farms/{farmId}/transfer | Create farm transfer request
[**farms_get**](FarmsApi.md#farms_get) | **GET** /farms | List of accessed farms
[**farms_incoming_confirm_post**](FarmsApi.md#farms_incoming_confirm_post) | **POST** /farms/incoming/confirm | Confirm transfer request
[**farms_incoming_get**](FarmsApi.md#farms_incoming_get) | **GET** /farms/incoming | Get incoming farm transfer requests
[**farms_incoming_reject_post**](FarmsApi.md#farms_incoming_reject_post) | **POST** /farms/incoming/reject | Reject transfer request
[**farms_post**](FarmsApi.md#farms_post) | **POST** /farms | Create new farm
[**farms_transfers_get**](FarmsApi.md#farms_transfers_get) | **GET** /farms/transfers | Get active transfers requests of all available farms


# **farms_delete**
> farms_delete(body=body)

Delete multiple farms

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
body = swagger_client.IDs() # IDs |  (optional)

try:
    # Delete multiple farms
    api_instance.farms_delete(body=body)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_delete: %s\n" % e)
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

# **farms_farm_id_configs_config_get**
> FarmConfigFiles farms_farm_id_configs_config_get(farm_id, config)

Get configuration file for farm

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
config = 'config_example' # str | 

try:
    # Get configuration file for farm
    api_response = api_instance.farms_farm_id_configs_config_get(farm_id, config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_farm_id_configs_config_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **config** | **str**|  | 

### Return type

[**FarmConfigFiles**](FarmConfigFiles.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_configs_get**
> FarmConfigFiles farms_farm_id_configs_get(farm_id)

Get configuration files for farm

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 

try:
    # Get configuration files for farm
    api_response = api_instance.farms_farm_id_configs_get(farm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_farm_id_configs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 

### Return type

[**FarmConfigFiles**](FarmConfigFiles.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_delete**
> farms_farm_id_delete(farm_id)

Delete farm

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 

try:
    # Delete farm
    api_instance.farms_farm_id_delete(farm_id)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_farm_id_delete: %s\n" % e)
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

# **farms_farm_id_deposit_address_get**
> object farms_farm_id_deposit_address_get(farm_id)

Get list of generated payment addresses

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 

try:
    # Get list of generated payment addresses
    api_response = api_instance.farms_farm_id_deposit_address_get(farm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_farm_id_deposit_address_get: %s\n" % e)
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

# **farms_farm_id_deposit_address_post**
> DepositAddress farms_farm_id_deposit_address_post(farm_id, body=body)

Generate payment address for deposits

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.DepositAddressCreateRequest() # DepositAddressCreateRequest |  (optional)

try:
    # Generate payment address for deposits
    api_response = api_instance.farms_farm_id_deposit_address_post(farm_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_farm_id_deposit_address_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**DepositAddressCreateRequest**](DepositAddressCreateRequest.md)|  | [optional] 

### Return type

[**DepositAddress**](DepositAddress.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_deposit_post**
> farms_farm_id_deposit_post(farm_id, body=body)

Make deposit to the farm from account balance

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.Deposit() # Deposit |  (optional)

try:
    # Make deposit to the farm from account balance
    api_instance.farms_farm_id_deposit_post(farm_id, body=body)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_farm_id_deposit_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**Deposit**](Deposit.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_events_get**
> object farms_farm_id_events_get(farm_id, page=page, per_page=per_page, type_id=type_id, exclude_type_id=exclude_type_id, worker_id=worker_id, config_type=config_type, search=search, user=user, start_date=start_date, end_date=end_date, group=group, group_id=group_id)

Farm events

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
page = 1 # int | Page number (optional) (default to 1)
per_page = 56 # int | Per-page count (default is 15) (optional)
type_id = 'type_id_example' # str | Return only records of these types, comma-separated list of IDs (optional)
exclude_type_id = 'exclude_type_id_example' # str | Exclude records of these types, comma-separated list of IDs (optional)
worker_id = 'worker_id_example' # str | Return only records for these workers, comma-separated list of IDs (optional)
config_type = 'config_type_example' # str | Comma-separated list of config types (optional)
search = 'search_example' # str | String with searched value (optional)
user = 'user_example' # str | Filter by user. Both login and name are used for searching. This filter is searching by \"contains\", not \"equals\". (optional)
start_date = 'start_date_example' # str | Start date (optional)
end_date = 'end_date_example' # str | End date (inclusive) (optional)
group = 0 # int | Output grouped events when possible (optional) (default to 0)
group_id = 56 # int | Output events cotained in this group (optional)

try:
    # Farm events
    api_response = api_instance.farms_farm_id_events_get(farm_id, page=page, per_page=per_page, type_id=type_id, exclude_type_id=exclude_type_id, worker_id=worker_id, config_type=config_type, search=search, user=user, start_date=start_date, end_date=end_date, group=group, group_id=group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_farm_id_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Per-page count (default is 15) | [optional] 
 **type_id** | **str**| Return only records of these types, comma-separated list of IDs | [optional] 
 **exclude_type_id** | **str**| Exclude records of these types, comma-separated list of IDs | [optional] 
 **worker_id** | **str**| Return only records for these workers, comma-separated list of IDs | [optional] 
 **config_type** | **str**| Comma-separated list of config types | [optional] 
 **search** | **str**| String with searched value | [optional] 
 **user** | **str**| Filter by user. Both login and name are used for searching. This filter is searching by \&quot;contains\&quot;, not \&quot;equals\&quot;. | [optional] 
 **start_date** | **str**| Start date | [optional] 
 **end_date** | **str**| End date (inclusive) | [optional] 
 **group** | **int**| Output grouped events when possible | [optional] [default to 0]
 **group_id** | **int**| Output events cotained in this group | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_get**
> Farm farms_farm_id_get(farm_id)

Farm info

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 

try:
    # Farm info
    api_response = api_instance.farms_farm_id_get(farm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_farm_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 

### Return type

[**Farm**](Farm.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_invoice_get**
> file farms_farm_id_invoice_get(farm_id, start_date=start_date, end_date=end_date)

Generate invoice for specified period

If period is not set - invoice for last month will be generated.

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
start_date = 'start_date_example' # str | Start date (optional)
end_date = 'end_date_example' # str | End date (inclusive) (optional)

try:
    # Generate invoice for specified period
    api_response = api_instance.farms_farm_id_invoice_get(farm_id, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_farm_id_invoice_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **start_date** | **str**| Start date | [optional] 
 **end_date** | **str**| End date (inclusive) | [optional] 

### Return type

[**file**](file.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_metrics_get**
> object farms_farm_id_metrics_get(farm_id, _date=_date, period=period, fill_gaps=fill_gaps)

Farm metrics

Provides metrics for current farm. Data is refreshed every 5 minutes. For 1 week period - metrics are downsampled by 15 minutes. For 1 month period - metrics are downsampled by 1 hour. 

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
_date = 'today' # str | Start date (optional) (default to today)
period = '1d' # str | Period (1 day, 1 week, 1 month) (optional) (default to 1d)
fill_gaps = 0 # int | Fill gaps with empty points (optional) (default to 0)

try:
    # Farm metrics
    api_response = api_instance.farms_farm_id_metrics_get(farm_id, _date=_date, period=period, fill_gaps=fill_gaps)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_farm_id_metrics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
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

# **farms_farm_id_notifications_get**
> object farms_farm_id_notifications_get(farm_id)

Get notifications settings

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 

try:
    # Get notifications settings
    api_response = api_instance.farms_farm_id_notifications_get(farm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_farm_id_notifications_get: %s\n" % e)
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

# **farms_farm_id_notifications_patch**
> farms_farm_id_notifications_patch(farm_id, body=body)

Update notifications settings

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.NotificationSubscriptionsFarm() # NotificationSubscriptionsFarm |  (optional)

try:
    # Update notifications settings
    api_instance.farms_farm_id_notifications_patch(farm_id, body=body)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_farm_id_notifications_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**NotificationSubscriptionsFarm**](NotificationSubscriptionsFarm.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_patch**
> farms_farm_id_patch(farm_id, body=body)

Edit farm

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.FarmUpdateRequest() # FarmUpdateRequest |  (optional)

try:
    # Edit farm
    api_instance.farms_farm_id_patch(farm_id, body=body)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_farm_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**FarmUpdateRequest**](FarmUpdateRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_payer_delete**
> farms_farm_id_payer_delete(farm_id)

Unassign farm payer and restore default value

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 

try:
    # Unassign farm payer and restore default value
    api_instance.farms_farm_id_payer_delete(farm_id)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_farm_id_payer_delete: %s\n" % e)
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

# **farms_farm_id_personal_settings_patch**
> farms_farm_id_personal_settings_patch(farm_id, body=body)

Update personal settings for the farm

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.FarmPersonalSettings() # FarmPersonalSettings |  (optional)

try:
    # Update personal settings for the farm
    api_instance.farms_farm_id_personal_settings_patch(farm_id, body=body)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_farm_id_personal_settings_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**FarmPersonalSettings**](FarmPersonalSettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_power_report_get**
> file farms_farm_id_power_report_get(farm_id, start_date, period, action, worker_ids=worker_ids)

Generate report about power consumption for specified period

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
start_date = 'start_date_example' # str | Start date
period = 'period_example' # str | The period for which the report will be generated.
action = 'action_example' # str | The action with report after generation.
worker_ids = 'worker_ids_example' # str | Comma-separated list of worker ids for generating workers-specific report (optional)

try:
    # Generate report about power consumption for specified period
    api_response = api_instance.farms_farm_id_power_report_get(farm_id, start_date, period, action, worker_ids=worker_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_farm_id_power_report_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **start_date** | **str**| Start date | 
 **period** | **str**| The period for which the report will be generated. | 
 **action** | **str**| The action with report after generation. | 
 **worker_ids** | **str**| Comma-separated list of worker ids for generating workers-specific report | [optional] 

### Return type

[**file**](file.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_send_money_post**
> farms_farm_id_send_money_post(farm_id, body=body)

Send money to user

This action requires Security code.

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
# Configure API key authorization: SecurityCode
configuration = swagger_client.Configuration()
configuration.api_key['X-Security-Code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Security-Code'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.Body() # Body |  (optional)

try:
    # Send money to user
    api_instance.farms_farm_id_send_money_post(farm_id, body=body)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_farm_id_send_money_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**Body**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [SecurityCode](../README.md#SecurityCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_stats_get**
> object farms_farm_id_stats_get(farm_id, search_id=search_id, worker_ids=worker_ids)

Farm stats

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
search_id = 'search_id_example' # str | ID of cached workers selection (optional)
worker_ids = 'worker_ids_example' # str | Calculate stats only for these workers. Comma-separated IDs list. (optional)

try:
    # Farm stats
    api_response = api_instance.farms_farm_id_stats_get(farm_id, search_id=search_id, worker_ids=worker_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_farm_id_stats_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **search_id** | **str**| ID of cached workers selection | [optional] 
 **worker_ids** | **str**| Calculate stats only for these workers. Comma-separated IDs list. | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_transactions_get**
> object farms_farm_id_transactions_get(farm_id, page=page, per_page=per_page, type_id=type_id, exclude_type_id=exclude_type_id)

Transactions history

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
page = 1 # int | Page number (optional) (default to 1)
per_page = 56 # int | Per-page count (default is 15) (optional)
type_id = 'type_id_example' # str | Return only records of these types, comma-separated list of IDs (optional)
exclude_type_id = 'exclude_type_id_example' # str | Exclude records of these types, comma-separated list of IDs (optional)

try:
    # Transactions history
    api_response = api_instance.farms_farm_id_transactions_get(farm_id, page=page, per_page=per_page, type_id=type_id, exclude_type_id=exclude_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_farm_id_transactions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Per-page count (default is 15) | [optional] 
 **type_id** | **str**| Return only records of these types, comma-separated list of IDs | [optional] 
 **exclude_type_id** | **str**| Exclude records of these types, comma-separated list of IDs | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_transfer_delete**
> farms_farm_id_transfer_delete(farm_id)

Cancel farm transfer request

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 

try:
    # Cancel farm transfer request
    api_instance.farms_farm_id_transfer_delete(farm_id)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_farm_id_transfer_delete: %s\n" % e)
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

# **farms_farm_id_transfer_get**
> FarmTransfer farms_farm_id_transfer_get(farm_id)

Get active farm transfer request

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 

try:
    # Get active farm transfer request
    api_response = api_instance.farms_farm_id_transfer_get(farm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_farm_id_transfer_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 

### Return type

[**FarmTransfer**](FarmTransfer.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_transfer_post**
> FarmTransfer farms_farm_id_transfer_post(farm_id, body=body)

Create farm transfer request

This action sends a request to target user and the farm will be transferred when that user confirm the request. 

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.Body() # Body |  (optional)

try:
    # Create farm transfer request
    api_response = api_instance.farms_farm_id_transfer_post(farm_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_farm_id_transfer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**Body**](.md)|  | [optional] 

### Return type

[**FarmTransfer**](FarmTransfer.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_get**
> object farms_get()

List of accessed farms

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))

try:
    # List of accessed farms
    api_response = api_instance.farms_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_get: %s\n" % e)
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

# **farms_incoming_confirm_post**
> farms_incoming_confirm_post(body)

Confirm transfer request

This action must be performed by user who received transfer request.

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body() # Body | 

try:
    # Confirm transfer request
    api_instance.farms_incoming_confirm_post(body)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_incoming_confirm_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_incoming_get**
> object farms_incoming_get(farm_id)

Get incoming farm transfer requests

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 

try:
    # Get incoming farm transfer requests
    api_response = api_instance.farms_incoming_get(farm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_incoming_get: %s\n" % e)
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

# **farms_incoming_reject_post**
> farms_incoming_reject_post(body)

Reject transfer request

This action must be performed by user who received transfer request.

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body() # Body | 

try:
    # Reject transfer request
    api_instance.farms_incoming_reject_post(body)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_incoming_reject_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_post**
> Farm farms_post(body=body)

Create new farm

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))
body = swagger_client.FarmCreateRequest() # FarmCreateRequest |  (optional)

try:
    # Create new farm
    api_response = api_instance.farms_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FarmCreateRequest**](FarmCreateRequest.md)|  | [optional] 

### Return type

[**Farm**](Farm.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_transfers_get**
> object farms_transfers_get()

Get active transfers requests of all available farms

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
api_instance = swagger_client.FarmsApi(swagger_client.ApiClient(configuration))

try:
    # Get active transfers requests of all available farms
    api_response = api_instance.farms_transfers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FarmsApi->farms_transfers_get: %s\n" % e)
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

