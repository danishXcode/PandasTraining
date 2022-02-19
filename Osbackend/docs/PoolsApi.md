# swagger_client.PoolsApi

All URIs are relative to *https://api2.hiveos.farm/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pools_by_coin_coin_get**](PoolsApi.md#pools_by_coin_coin_get) | **GET** /pools/by_coin/{coin} | Pool templates which suit coin name
[**pools_by_name_pool_get**](PoolsApi.md#pools_by_name_pool_get) | **GET** /pools/by_name/{pool} | Pool templates
[**pools_get**](PoolsApi.md#pools_get) | **GET** /pools | Available pools list and coins that we have in pools


# **pools_by_coin_coin_get**
> object pools_by_coin_coin_get(coin)

Pool templates which suit coin name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoolsApi()
coin = 'coin_example' # str | Coin name like \"ETH\"

try:
    # Pool templates which suit coin name
    api_response = api_instance.pools_by_coin_coin_get(coin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->pools_by_coin_coin_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coin** | **str**| Coin name like \&quot;ETH\&quot; | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pools_by_name_pool_get**
> object pools_by_name_pool_get(pool)

Pool templates

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoolsApi()
pool = 'pool_example' # str | Pool name like \"nanopool\"

try:
    # Pool templates
    api_response = api_instance.pools_by_name_pool_get(pool)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->pools_by_name_pool_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool** | **str**| Pool name like \&quot;nanopool\&quot; | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pools_get**
> object pools_get()

Available pools list and coins that we have in pools

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoolsApi()

try:
    # Available pools list and coins that we have in pools
    api_response = api_instance.pools_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->pools_get: %s\n" % e)
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

