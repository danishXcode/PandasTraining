# swagger_client.WalletsApi

All URIs are relative to *https://api2.hiveos.farm/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**farms_farm_id_wallets_delete**](WalletsApi.md#farms_farm_id_wallets_delete) | **DELETE** /farms/{farmId}/wallets | Delete multiple wallets
[**farms_farm_id_wallets_get**](WalletsApi.md#farms_farm_id_wallets_get) | **GET** /farms/{farmId}/wallets | Wallets list
[**farms_farm_id_wallets_post**](WalletsApi.md#farms_farm_id_wallets_post) | **POST** /farms/{farmId}/wallets | Create new wallet
[**farms_farm_id_wallets_wallet_id_delete**](WalletsApi.md#farms_farm_id_wallets_wallet_id_delete) | **DELETE** /farms/{farmId}/wallets/{walletId} | Delete wallet
[**farms_farm_id_wallets_wallet_id_get**](WalletsApi.md#farms_farm_id_wallets_wallet_id_get) | **GET** /farms/{farmId}/wallets/{walletId} | Wallet info
[**farms_farm_id_wallets_wallet_id_patch**](WalletsApi.md#farms_farm_id_wallets_wallet_id_patch) | **PATCH** /farms/{farmId}/wallets/{walletId} | Edit wallet
[**wallets_delete**](WalletsApi.md#wallets_delete) | **DELETE** /wallets | Delete multiple wallets
[**wallets_get**](WalletsApi.md#wallets_get) | **GET** /wallets | Wallets list
[**wallets_post**](WalletsApi.md#wallets_post) | **POST** /wallets | Create new wallet
[**wallets_wallet_id_delete**](WalletsApi.md#wallets_wallet_id_delete) | **DELETE** /wallets/{walletId} | Delete wallet
[**wallets_wallet_id_get**](WalletsApi.md#wallets_wallet_id_get) | **GET** /wallets/{walletId} | Wallet info
[**wallets_wallet_id_patch**](WalletsApi.md#wallets_wallet_id_patch) | **PATCH** /wallets/{walletId} | Edit wallet


# **farms_farm_id_wallets_delete**
> farms_farm_id_wallets_delete(farm_id, body=body)

Delete multiple wallets

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
api_instance = swagger_client.WalletsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.IDs() # IDs |  (optional)

try:
    # Delete multiple wallets
    api_instance.farms_farm_id_wallets_delete(farm_id, body=body)
except ApiException as e:
    print("Exception when calling WalletsApi->farms_farm_id_wallets_delete: %s\n" % e)
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

# **farms_farm_id_wallets_get**
> object farms_farm_id_wallets_get(farm_id)

Wallets list

Returns wallets that belong to given farm along with wallets that belong to farm's owner

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
api_instance = swagger_client.WalletsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 

try:
    # Wallets list
    api_response = api_instance.farms_farm_id_wallets_get(farm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletsApi->farms_farm_id_wallets_get: %s\n" % e)
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

# **farms_farm_id_wallets_post**
> WalletF farms_farm_id_wallets_post(farm_id, body=body)

Create new wallet

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
api_instance = swagger_client.WalletsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.WalletCreateRequest() # WalletCreateRequest |  (optional)

try:
    # Create new wallet
    api_response = api_instance.farms_farm_id_wallets_post(farm_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletsApi->farms_farm_id_wallets_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**WalletCreateRequest**](WalletCreateRequest.md)|  | [optional] 

### Return type

[**WalletF**](WalletF.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_wallets_wallet_id_delete**
> farms_farm_id_wallets_wallet_id_delete(farm_id, wallet_id)

Delete wallet

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
api_instance = swagger_client.WalletsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
wallet_id = 56 # int | 

try:
    # Delete wallet
    api_instance.farms_farm_id_wallets_wallet_id_delete(farm_id, wallet_id)
except ApiException as e:
    print("Exception when calling WalletsApi->farms_farm_id_wallets_wallet_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **wallet_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_wallets_wallet_id_get**
> WalletF farms_farm_id_wallets_wallet_id_get(farm_id, wallet_id)

Wallet info

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
api_instance = swagger_client.WalletsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
wallet_id = 56 # int | 

try:
    # Wallet info
    api_response = api_instance.farms_farm_id_wallets_wallet_id_get(farm_id, wallet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletsApi->farms_farm_id_wallets_wallet_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **wallet_id** | **int**|  | 

### Return type

[**WalletF**](WalletF.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_wallets_wallet_id_patch**
> farms_farm_id_wallets_wallet_id_patch(farm_id, wallet_id, body=body)

Edit wallet

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
api_instance = swagger_client.WalletsApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
wallet_id = 56 # int | 
body = swagger_client.WalletUpdateRequest() # WalletUpdateRequest |  (optional)

try:
    # Edit wallet
    api_instance.farms_farm_id_wallets_wallet_id_patch(farm_id, wallet_id, body=body)
except ApiException as e:
    print("Exception when calling WalletsApi->farms_farm_id_wallets_wallet_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **wallet_id** | **int**|  | 
 **body** | [**WalletUpdateRequest**](WalletUpdateRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallets_delete**
> wallets_delete(body=body)

Delete multiple wallets

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
api_instance = swagger_client.WalletsApi(swagger_client.ApiClient(configuration))
body = swagger_client.IDs() # IDs |  (optional)

try:
    # Delete multiple wallets
    api_instance.wallets_delete(body=body)
except ApiException as e:
    print("Exception when calling WalletsApi->wallets_delete: %s\n" % e)
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

# **wallets_get**
> object wallets_get()

Wallets list

Returns wallets that belong to current user

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
api_instance = swagger_client.WalletsApi(swagger_client.ApiClient(configuration))

try:
    # Wallets list
    api_response = api_instance.wallets_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletsApi->wallets_get: %s\n" % e)
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

# **wallets_post**
> WalletU wallets_post(body=body)

Create new wallet

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
api_instance = swagger_client.WalletsApi(swagger_client.ApiClient(configuration))
body = swagger_client.WalletCreateRequest() # WalletCreateRequest |  (optional)

try:
    # Create new wallet
    api_response = api_instance.wallets_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletsApi->wallets_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WalletCreateRequest**](WalletCreateRequest.md)|  | [optional] 

### Return type

[**WalletU**](WalletU.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallets_wallet_id_delete**
> wallets_wallet_id_delete(wallet_id)

Delete wallet

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
api_instance = swagger_client.WalletsApi(swagger_client.ApiClient(configuration))
wallet_id = 56 # int | 

try:
    # Delete wallet
    api_instance.wallets_wallet_id_delete(wallet_id)
except ApiException as e:
    print("Exception when calling WalletsApi->wallets_wallet_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallets_wallet_id_get**
> WalletU wallets_wallet_id_get(wallet_id)

Wallet info

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
api_instance = swagger_client.WalletsApi(swagger_client.ApiClient(configuration))
wallet_id = 56 # int | 

try:
    # Wallet info
    api_response = api_instance.wallets_wallet_id_get(wallet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletsApi->wallets_wallet_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **int**|  | 

### Return type

[**WalletU**](WalletU.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallets_wallet_id_patch**
> wallets_wallet_id_patch(wallet_id, body=body)

Edit wallet

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
api_instance = swagger_client.WalletsApi(swagger_client.ApiClient(configuration))
wallet_id = 56 # int | 
body = swagger_client.WalletUpdateRequest() # WalletUpdateRequest |  (optional)

try:
    # Edit wallet
    api_instance.wallets_wallet_id_patch(wallet_id, body=body)
except ApiException as e:
    print("Exception when calling WalletsApi->wallets_wallet_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **int**|  | 
 **body** | [**WalletUpdateRequest**](WalletUpdateRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

