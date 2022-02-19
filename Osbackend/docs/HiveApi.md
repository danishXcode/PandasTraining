# swagger_client.HiveApi

All URIs are relative to *https://api2.hiveos.farm/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hive_algos_get**](HiveApi.md#hive_algos_get) | **GET** /hive/algos | List of available algorithms
[**hive_asic_firmwares_get**](HiveApi.md#hive_asic_firmwares_get) | **GET** /hive/asic_firmwares | Get ASIC firmwares list
[**hive_coins_get**](HiveApi.md#hive_coins_get) | **GET** /hive/coins | List of available coins
[**hive_currencies_get**](HiveApi.md#hive_currencies_get) | **GET** /hive/currencies | Get list of currencies that are used in deposits and referral payments.
[**hive_deposit_address_providers_get**](HiveApi.md#hive_deposit_address_providers_get) | **GET** /hive/deposit_address_providers | Get list of deposit address providers with options.
[**hive_miners_get**](HiveApi.md#hive_miners_get) | **GET** /hive/miners | List of available miners
[**hive_mirror_urls_get**](HiveApi.md#hive_mirror_urls_get) | **GET** /hive/mirror_urls | List of mirror URLs
[**hive_notification_channels_get**](HiveApi.md#hive_notification_channels_get) | **GET** /hive/notification_channels | Get list of supported notification channels
[**hive_overclocks_get**](HiveApi.md#hive_overclocks_get) | **GET** /hive/overclocks | Get popular overclock settings for different GPUs and algos. Result is sorted by rating.
[**hive_pricing_get**](HiveApi.md#hive_pricing_get) | **GET** /hive/pricing | Get pricing information
[**hive_stats_get**](HiveApi.md#hive_stats_get) | **GET** /hive/stats | Get Hive statistics
[**hive_versions_get**](HiveApi.md#hive_versions_get) | **GET** /hive/versions | Hive or Asic Hub changelog
[**hive_versions_system_type_version_get**](HiveApi.md#hive_versions_system_type_version_get) | **GET** /hive/versions/{systemType}/{version} | Hive version info
[**hive_wallet_sources_get**](HiveApi.md#hive_wallet_sources_get) | **GET** /hive/wallet_sources | List of supported wallet sources


# **hive_algos_get**
> object hive_algos_get()

List of available algorithms

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HiveApi()

try:
    # List of available algorithms
    api_response = api_instance.hive_algos_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HiveApi->hive_algos_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hive_asic_firmwares_get**
> object hive_asic_firmwares_get()

Get ASIC firmwares list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HiveApi()

try:
    # Get ASIC firmwares list
    api_response = api_instance.hive_asic_firmwares_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HiveApi->hive_asic_firmwares_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hive_coins_get**
> object hive_coins_get()

List of available coins

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HiveApi()

try:
    # List of available coins
    api_response = api_instance.hive_coins_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HiveApi->hive_coins_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hive_currencies_get**
> object hive_currencies_get()

Get list of currencies that are used in deposits and referral payments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HiveApi()

try:
    # Get list of currencies that are used in deposits and referral payments.
    api_response = api_instance.hive_currencies_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HiveApi->hive_currencies_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hive_deposit_address_providers_get**
> object hive_deposit_address_providers_get()

Get list of deposit address providers with options.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HiveApi()

try:
    # Get list of deposit address providers with options.
    api_response = api_instance.hive_deposit_address_providers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HiveApi->hive_deposit_address_providers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hive_miners_get**
> object hive_miners_get()

List of available miners

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HiveApi()

try:
    # List of available miners
    api_response = api_instance.hive_miners_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HiveApi->hive_miners_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hive_mirror_urls_get**
> object hive_mirror_urls_get()

List of mirror URLs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HiveApi()

try:
    # List of mirror URLs
    api_response = api_instance.hive_mirror_urls_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HiveApi->hive_mirror_urls_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hive_notification_channels_get**
> object hive_notification_channels_get()

Get list of supported notification channels

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HiveApi()

try:
    # Get list of supported notification channels
    api_response = api_instance.hive_notification_channels_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HiveApi->hive_notification_channels_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hive_overclocks_get**
> object hive_overclocks_get(gpu_brand=gpu_brand, gpu_model=gpu_model, gpu_mem=gpu_mem, algo=algo, page=page, per_page=per_page)

Get popular overclock settings for different GPUs and algos. Result is sorted by rating.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HiveApi()
gpu_brand = 'gpu_brand_example' # str | Filter by GPU brand (optional)
gpu_model = 'gpu_model_example' # str | Filter by GPU model (optional)
gpu_mem = 'gpu_mem_example' # str | Filter by GPU memory (optional)
algo = 'algo_example' # str | Filter by algo (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 56 # int | Per-page count (default is 15) (optional)

try:
    # Get popular overclock settings for different GPUs and algos. Result is sorted by rating.
    api_response = api_instance.hive_overclocks_get(gpu_brand=gpu_brand, gpu_model=gpu_model, gpu_mem=gpu_mem, algo=algo, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HiveApi->hive_overclocks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gpu_brand** | **str**| Filter by GPU brand | [optional] 
 **gpu_model** | **str**| Filter by GPU model | [optional] 
 **gpu_mem** | **str**| Filter by GPU memory | [optional] 
 **algo** | **str**| Filter by algo | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Per-page count (default is 15) | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hive_pricing_get**
> object hive_pricing_get()

Get pricing information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HiveApi()

try:
    # Get pricing information
    api_response = api_instance.hive_pricing_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HiveApi->hive_pricing_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hive_stats_get**
> object hive_stats_get()

Get Hive statistics

Returns different proportional data. These statistics are updated once a day based on online workers for the moment. Items with amount < 0.01% is not included in the result, so they should be considered as \"other\". 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HiveApi()

try:
    # Get Hive statistics
    api_response = api_instance.hive_stats_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HiveApi->hive_stats_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hive_versions_get**
> object hive_versions_get(type=type, page=page, per_page=per_page)

Hive or Asic Hub changelog

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HiveApi()
type = 'type_example' # str | Release versions type. os for Hive releases and asic_hub for Asic Hub releases (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 56 # int | Per-page count (default is 15) (optional)

try:
    # Hive or Asic Hub changelog
    api_response = api_instance.hive_versions_get(type=type, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HiveApi->hive_versions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Release versions type. os for Hive releases and asic_hub for Asic Hub releases | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Per-page count (default is 15) | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hive_versions_system_type_version_get**
> HiveVersion hive_versions_system_type_version_get(system_type, version)

Hive version info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HiveApi()
system_type = 'system_type_example' # str | System type
version = 'version_example' # str | Version number

try:
    # Hive version info
    api_response = api_instance.hive_versions_system_type_version_get(system_type, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HiveApi->hive_versions_system_type_version_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_type** | **str**| System type | 
 **version** | **str**| Version number | 

### Return type

[**HiveVersion**](HiveVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hive_wallet_sources_get**
> object hive_wallet_sources_get()

List of supported wallet sources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HiveApi()

try:
    # List of supported wallet sources
    api_response = api_instance.hive_wallet_sources_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HiveApi->hive_wallet_sources_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

