# swagger_client.AccountApi

All URIs are relative to *https://api2.hiveos.farm/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_access_patch**](AccountApi.md#account_access_patch) | **PATCH** /account/access | Update account access settings
[**account_activate_post**](AccountApi.md#account_activate_post) | **POST** /account/activate | Activate registered account
[**account_announcements_announcement_id_hide_post**](AccountApi.md#account_announcements_announcement_id_hide_post) | **POST** /account/announcements/{announcementId}/hide | Hide announcement (mark as read)
[**account_announcements_get**](AccountApi.md#account_announcements_get) | **GET** /account/announcements | List of unread announcements
[**account_delete**](AccountApi.md#account_delete) | **DELETE** /account | Delete account
[**account_deposit_address_get**](AccountApi.md#account_deposit_address_get) | **GET** /account/deposit/address | Get list of generated payment addresses
[**account_deposit_address_post**](AccountApi.md#account_deposit_address_post) | **POST** /account/deposit/address | Generate payment address for deposits
[**account_deposit_coinpayments_get**](AccountApi.md#account_deposit_coinpayments_get) | **GET** /account/deposit/coinpayments | Get request data for submitting to coinpayments system
[**account_email_confirm_post**](AccountApi.md#account_email_confirm_post) | **POST** /account/email/confirm | Confirm current email
[**account_email_confirmation_post**](AccountApi.md#account_email_confirmation_post) | **POST** /account/email/confirmation | Request an email confirmation token
[**account_events_get**](AccountApi.md#account_events_get) | **GET** /account/events | Account events
[**account_get**](AccountApi.md#account_get) | **GET** /account | Get full account info
[**account_meta_get**](AccountApi.md#account_meta_get) | **GET** /account/meta | Get all meta data from all namespaces
[**account_meta_namespace_delete**](AccountApi.md#account_meta_namespace_delete) | **DELETE** /account/meta/{namespace} | Delete the whole meta data namespace
[**account_meta_namespace_get**](AccountApi.md#account_meta_namespace_get) | **GET** /account/meta/{namespace} | Get meta data from namespace
[**account_meta_namespace_patch**](AccountApi.md#account_meta_namespace_patch) | **PATCH** /account/meta/{namespace} | Merge existing meta in namespace with provided data
[**account_meta_namespace_put**](AccountApi.md#account_meta_namespace_put) | **PUT** /account/meta/{namespace} | Replace the whole meta in namespace with provided data
[**account_notifications_channel_delete**](AccountApi.md#account_notifications_channel_delete) | **DELETE** /account/notifications/{channel} | Unsubscribe from Hive Bot notifications
[**account_notifications_channel_post**](AccountApi.md#account_notifications_channel_post) | **POST** /account/notifications/{channel} | Subscribe to Hive Bot notifications
[**account_notifications_get**](AccountApi.md#account_notifications_get) | **GET** /account/notifications | Get notifications settings
[**account_notifications_patch**](AccountApi.md#account_notifications_patch) | **PATCH** /account/notifications | Update notifications settings
[**account_password_put**](AccountApi.md#account_password_put) | **PUT** /account/password | Change password
[**account_password_reset_post**](AccountApi.md#account_password_reset_post) | **POST** /account/password/reset | Request password reset
[**account_password_reset_put**](AccountApi.md#account_password_reset_put) | **PUT** /account/password/reset | Reset password
[**account_payments_get**](AccountApi.md#account_payments_get) | **GET** /account/payments | Account payments history
[**account_post**](AccountApi.md#account_post) | **POST** /account | Create account (registration)
[**account_profile_get**](AccountApi.md#account_profile_get) | **GET** /account/profile | Get profile infirmation
[**account_profile_patch**](AccountApi.md#account_profile_patch) | **PATCH** /account/profile | Update profile
[**account_referral_balances_get**](AccountApi.md#account_referral_balances_get) | **GET** /account/referral/balances | Get referral balances
[**account_referral_payout_addresses_get**](AccountApi.md#account_referral_payout_addresses_get) | **GET** /account/referral/payout_addresses | Get payout addresses
[**account_referral_payout_addresses_put**](AccountApi.md#account_referral_payout_addresses_put) | **PUT** /account/referral/payout_addresses | Update payout addresses
[**account_referral_payout_to_account_post**](AccountApi.md#account_referral_payout_to_account_post) | **POST** /account/referral/payout_to_account | Make a payout to hive account
[**account_referral_promocode_put**](AccountApi.md#account_referral_promocode_put) | **PUT** /account/referral/promocode | Update promo code
[**account_send_money_post**](AccountApi.md#account_send_money_post) | **POST** /account/send_money | Send money to another user
[**account_tokens_get**](AccountApi.md#account_tokens_get) | **GET** /account/tokens | Get list of auth tokens
[**account_tokens_post**](AccountApi.md#account_tokens_post) | **POST** /account/tokens | Create new personal auth token
[**account_tokens_session_delete**](AccountApi.md#account_tokens_session_delete) | **DELETE** /account/tokens/session | Delete all session tokens except current.
[**account_tokens_token_id_delete**](AccountApi.md#account_tokens_token_id_delete) | **DELETE** /account/tokens/{tokenId} | Delete auth token
[**account_tokens_token_id_get**](AccountApi.md#account_tokens_token_id_get) | **GET** /account/tokens/{tokenId} | Get auth token info
[**account_tokens_token_id_patch**](AccountApi.md#account_tokens_token_id_patch) | **PATCH** /account/tokens/{tokenId} | Edit auth token
[**account_transactions_get**](AccountApi.md#account_transactions_get) | **GET** /account/transactions | Account transactions history
[**account_twofa_delete**](AccountApi.md#account_twofa_delete) | **DELETE** /account/twofa | Disable Two Factor Authentication (2FA)
[**account_twofa_post**](AccountApi.md#account_twofa_post) | **POST** /account/twofa | Enable Two Factor Authentication (2FA)
[**account_twofa_secret_get**](AccountApi.md#account_twofa_secret_get) | **GET** /account/twofa/secret | Generate secret code to enable Two Factor Authentication (2FA)


# **account_access_patch**
> account_access_patch(body=body)

Update account access settings

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccountAccess() # AccountAccess |  (optional)

try:
    # Update account access settings
    api_instance.account_access_patch(body=body)
except ApiException as e:
    print("Exception when calling AccountApi->account_access_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountAccess**](AccountAccess.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [SecurityCode](../README.md#SecurityCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_activate_post**
> object account_activate_post(body=body)

Activate registered account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()
body = swagger_client.Body() # Body |  (optional)

try:
    # Activate registered account
    api_response = api_instance.account_activate_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_activate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_announcements_announcement_id_hide_post**
> account_announcements_announcement_id_hide_post(announcement_id)

Hide announcement (mark as read)

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
announcement_id = 56 # int | 

try:
    # Hide announcement (mark as read)
    api_instance.account_announcements_announcement_id_hide_post(announcement_id)
except ApiException as e:
    print("Exception when calling AccountApi->account_announcements_announcement_id_hide_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **announcement_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_announcements_get**
> object account_announcements_get()

List of unread announcements

Announcements are messages from Hive OS team with important information such as scheduled downtime or technical issues. 

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))

try:
    # List of unread announcements
    api_response = api_instance.account_announcements_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_announcements_get: %s\n" % e)
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

# **account_delete**
> account_delete()

Delete account

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))

try:
    # Delete account
    api_instance.account_delete()
except ApiException as e:
    print("Exception when calling AccountApi->account_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [SecurityCode](../README.md#SecurityCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_deposit_address_get**
> object account_deposit_address_get()

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))

try:
    # Get list of generated payment addresses
    api_response = api_instance.account_deposit_address_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_deposit_address_get: %s\n" % e)
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

# **account_deposit_address_post**
> DepositAddress account_deposit_address_post(body=body)

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
body = swagger_client.DepositAddressCreateRequest() # DepositAddressCreateRequest |  (optional)

try:
    # Generate payment address for deposits
    api_response = api_instance.account_deposit_address_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_deposit_address_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DepositAddressCreateRequest**](DepositAddressCreateRequest.md)|  | [optional] 

### Return type

[**DepositAddress**](DepositAddress.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_deposit_coinpayments_get**
> object account_deposit_coinpayments_get(amount, farm_id=farm_id, success_url=success_url, cancel_url=cancel_url)

Get request data for submitting to coinpayments system

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
amount = 8.14 # float | Deposit amount in fiat currency
farm_id = 8.14 # float | Farm ID If set - after successful deposit in account the whole amount will be deposited in this farm  (optional)
success_url = 'success_url_example' # str | The URL to return after successful payment (optional)
cancel_url = 'cancel_url_example' # str | The URL to return in after payment cancellation (optional)

try:
    # Get request data for submitting to coinpayments system
    api_response = api_instance.account_deposit_coinpayments_get(amount, farm_id=farm_id, success_url=success_url, cancel_url=cancel_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_deposit_coinpayments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **float**| Deposit amount in fiat currency | 
 **farm_id** | **float**| Farm ID If set - after successful deposit in account the whole amount will be deposited in this farm  | [optional] 
 **success_url** | **str**| The URL to return after successful payment | [optional] 
 **cancel_url** | **str**| The URL to return in after payment cancellation | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_email_confirm_post**
> account_email_confirm_post(body=body)

Confirm current email

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body() # Body |  (optional)

try:
    # Confirm current email
    api_instance.account_email_confirm_post(body=body)
except ApiException as e:
    print("Exception when calling AccountApi->account_email_confirm_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_email_confirmation_post**
> account_email_confirmation_post(body=body)

Request an email confirmation token

This request generates a confirmation token and sends it to account's email address. The token is used for email address confirmation or account activation. * For activated accounts this request must be sent with authentication token without payload. * For non-activated accounts this request must be sent without authentication token with payload. 

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body() # Body |  (optional)

try:
    # Request an email confirmation token
    api_instance.account_email_confirmation_post(body=body)
except ApiException as e:
    print("Exception when calling AccountApi->account_email_confirmation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_events_get**
> object account_events_get(page=page, per_page=per_page, type_id=type_id, exclude_type_id=exclude_type_id, start_date=start_date, end_date=end_date)

Account events

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
per_page = 56 # int | Per-page count (default is 15) (optional)
type_id = 'type_id_example' # str | Return only records of these types, comma-separated list of IDs (optional)
exclude_type_id = 'exclude_type_id_example' # str | Exclude records of these types, comma-separated list of IDs (optional)
start_date = 'start_date_example' # str | Start date (optional)
end_date = 'end_date_example' # str | End date (inclusive) (optional)

try:
    # Account events
    api_response = api_instance.account_events_get(page=page, per_page=per_page, type_id=type_id, exclude_type_id=exclude_type_id, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Per-page count (default is 15) | [optional] 
 **type_id** | **str**| Return only records of these types, comma-separated list of IDs | [optional] 
 **exclude_type_id** | **str**| Exclude records of these types, comma-separated list of IDs | [optional] 
 **start_date** | **str**| Start date | [optional] 
 **end_date** | **str**| End date (inclusive) | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_get**
> Account account_get()

Get full account info

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))

try:
    # Get full account info
    api_response = api_instance.account_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Account**](Account.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_meta_get**
> object account_meta_get()

Get all meta data from all namespaces

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))

try:
    # Get all meta data from all namespaces
    api_response = api_instance.account_meta_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_meta_get: %s\n" % e)
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

# **account_meta_namespace_delete**
> account_meta_namespace_delete(namespace)

Delete the whole meta data namespace

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
namespace = 'namespace_example' # str | 

try:
    # Delete the whole meta data namespace
    api_instance.account_meta_namespace_delete(namespace)
except ApiException as e:
    print("Exception when calling AccountApi->account_meta_namespace_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_meta_namespace_get**
> object account_meta_namespace_get(namespace)

Get meta data from namespace

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
namespace = 'namespace_example' # str | 

try:
    # Get meta data from namespace
    api_response = api_instance.account_meta_namespace_get(namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_meta_namespace_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_meta_namespace_patch**
> account_meta_namespace_patch(namespace, body=body)

Merge existing meta in namespace with provided data

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
namespace = 'namespace_example' # str | 
body = NULL # object |  (optional)

try:
    # Merge existing meta in namespace with provided data
    api_instance.account_meta_namespace_patch(namespace, body=body)
except ApiException as e:
    print("Exception when calling AccountApi->account_meta_namespace_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **body** | **object**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_meta_namespace_put**
> account_meta_namespace_put(namespace, body=body)

Replace the whole meta in namespace with provided data

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
namespace = 'namespace_example' # str | 
body = NULL # object |  (optional)

try:
    # Replace the whole meta in namespace with provided data
    api_instance.account_meta_namespace_put(namespace, body=body)
except ApiException as e:
    print("Exception when calling AccountApi->account_meta_namespace_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 
 **body** | **object**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_notifications_channel_delete**
> account_notifications_channel_delete(channel)

Unsubscribe from Hive Bot notifications

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
channel = 'channel_example' # str | Channel name. Available channels can be get from `/hive/notification_channels` endpoint 

try:
    # Unsubscribe from Hive Bot notifications
    api_instance.account_notifications_channel_delete(channel)
except ApiException as e:
    print("Exception when calling AccountApi->account_notifications_channel_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel** | **str**| Channel name. Available channels can be get from &#x60;/hive/notification_channels&#x60; endpoint  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [SecurityCode](../README.md#SecurityCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_notifications_channel_post**
> account_notifications_channel_post(channel, body=body)

Subscribe to Hive Bot notifications

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
channel = 'channel_example' # str | Channel name. Available channels can be get from `/hive/notification_channels` endpoint 
body = swagger_client.Body() # Body |  (optional)

try:
    # Subscribe to Hive Bot notifications
    api_instance.account_notifications_channel_post(channel, body=body)
except ApiException as e:
    print("Exception when calling AccountApi->account_notifications_channel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel** | **str**| Channel name. Available channels can be get from &#x60;/hive/notification_channels&#x60; endpoint  | 
 **body** | [**Body**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [SecurityCode](../README.md#SecurityCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_notifications_get**
> object account_notifications_get()

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))

try:
    # Get notifications settings
    api_response = api_instance.account_notifications_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_notifications_get: %s\n" % e)
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

# **account_notifications_patch**
> account_notifications_patch(body=body)

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
body = swagger_client.NotificationSubscriptionsAccount() # NotificationSubscriptionsAccount |  (optional)

try:
    # Update notifications settings
    api_instance.account_notifications_patch(body=body)
except ApiException as e:
    print("Exception when calling AccountApi->account_notifications_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationSubscriptionsAccount**](NotificationSubscriptionsAccount.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_password_put**
> account_password_put(body=body)

Change password

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body() # Body |  (optional)

try:
    # Change password
    api_instance.account_password_put(body=body)
except ApiException as e:
    print("Exception when calling AccountApi->account_password_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [SecurityCode](../README.md#SecurityCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_password_reset_post**
> account_password_reset_post(body=body)

Request password reset

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()
body = swagger_client.Body() # Body |  (optional)

try:
    # Request password reset
    api_instance.account_password_reset_post(body=body)
except ApiException as e:
    print("Exception when calling AccountApi->account_password_reset_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_password_reset_put**
> AuthToken account_password_reset_put(body=body)

Reset password

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()
body = swagger_client.Body() # Body |  (optional)

try:
    # Reset password
    api_response = api_instance.account_password_reset_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_password_reset_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](.md)|  | [optional] 

### Return type

[**AuthToken**](AuthToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_payments_get**
> object account_payments_get()

Account payments history

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))

try:
    # Account payments history
    api_response = api_instance.account_payments_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_payments_get: %s\n" % e)
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

# **account_post**
> account_post(body=body)

Create account (registration)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()
body = swagger_client.SignupRequest() # SignupRequest |  (optional)

try:
    # Create account (registration)
    api_instance.account_post(body=body)
except ApiException as e:
    print("Exception when calling AccountApi->account_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SignupRequest**](SignupRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_profile_get**
> UserProfile account_profile_get()

Get profile infirmation

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))

try:
    # Get profile infirmation
    api_response = api_instance.account_profile_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_profile_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserProfile**](UserProfile.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_profile_patch**
> account_profile_patch(body=body)

Update profile

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserProfileFields() # UserProfileFields |  (optional)

try:
    # Update profile
    api_instance.account_profile_patch(body=body)
except ApiException as e:
    print("Exception when calling AccountApi->account_profile_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserProfileFields**](UserProfileFields.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_referral_balances_get**
> object account_referral_balances_get()

Get referral balances

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))

try:
    # Get referral balances
    api_response = api_instance.account_referral_balances_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_referral_balances_get: %s\n" % e)
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

# **account_referral_payout_addresses_get**
> object account_referral_payout_addresses_get()

Get payout addresses

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))

try:
    # Get payout addresses
    api_response = api_instance.account_referral_payout_addresses_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_referral_payout_addresses_get: %s\n" % e)
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

# **account_referral_payout_addresses_put**
> account_referral_payout_addresses_put(body=body)

Update payout addresses

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body() # Body |  (optional)

try:
    # Update payout addresses
    api_instance.account_referral_payout_addresses_put(body=body)
except ApiException as e:
    print("Exception when calling AccountApi->account_referral_payout_addresses_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [SecurityCode](../README.md#SecurityCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_referral_payout_to_account_post**
> object account_referral_payout_to_account_post(body=body)

Make a payout to hive account

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body() # Body |  (optional)

try:
    # Make a payout to hive account
    api_response = api_instance.account_referral_payout_to_account_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_referral_payout_to_account_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](.md)|  | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_referral_promocode_put**
> account_referral_promocode_put(body=body)

Update promo code

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body() # Body |  (optional)

try:
    # Update promo code
    api_instance.account_referral_promocode_put(body=body)
except ApiException as e:
    print("Exception when calling AccountApi->account_referral_promocode_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_send_money_post**
> account_send_money_post(body=body)

Send money to another user

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body() # Body |  (optional)

try:
    # Send money to another user
    api_instance.account_send_money_post(body=body)
except ApiException as e:
    print("Exception when calling AccountApi->account_send_money_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [SecurityCode](../README.md#SecurityCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_tokens_get**
> object account_tokens_get()

Get list of auth tokens

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))

try:
    # Get list of auth tokens
    api_response = api_instance.account_tokens_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_tokens_get: %s\n" % e)
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

# **account_tokens_post**
> AuthTokenItemFull account_tokens_post(body=body)

Create new personal auth token

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
body = swagger_client.AuthTokenItemCreateUpdateRequest() # AuthTokenItemCreateUpdateRequest |  (optional)

try:
    # Create new personal auth token
    api_response = api_instance.account_tokens_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_tokens_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthTokenItemCreateUpdateRequest**](AuthTokenItemCreateUpdateRequest.md)|  | [optional] 

### Return type

[**AuthTokenItemFull**](AuthTokenItemFull.md)

### Authorization

[ApiKey](../README.md#ApiKey), [SecurityCode](../README.md#SecurityCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_tokens_session_delete**
> account_tokens_session_delete()

Delete all session tokens except current.

Personal tokens are not affected.

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))

try:
    # Delete all session tokens except current.
    api_instance.account_tokens_session_delete()
except ApiException as e:
    print("Exception when calling AccountApi->account_tokens_session_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_tokens_token_id_delete**
> account_tokens_token_id_delete(token_id)

Delete auth token

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
token_id = 56 # int | 

try:
    # Delete auth token
    api_instance.account_tokens_token_id_delete(token_id)
except ApiException as e:
    print("Exception when calling AccountApi->account_tokens_token_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_tokens_token_id_get**
> AuthTokenItemFull account_tokens_token_id_get(token_id)

Get auth token info

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
token_id = 56 # int | 

try:
    # Get auth token info
    api_response = api_instance.account_tokens_token_id_get(token_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_tokens_token_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **int**|  | 

### Return type

[**AuthTokenItemFull**](AuthTokenItemFull.md)

### Authorization

[ApiKey](../README.md#ApiKey), [SecurityCode](../README.md#SecurityCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_tokens_token_id_patch**
> account_tokens_token_id_patch(token_id, body=body)

Edit auth token

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
token_id = 56 # int | 
body = swagger_client.AuthTokenItemCreateUpdateRequest() # AuthTokenItemCreateUpdateRequest |  (optional)

try:
    # Edit auth token
    api_instance.account_tokens_token_id_patch(token_id, body=body)
except ApiException as e:
    print("Exception when calling AccountApi->account_tokens_token_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **int**|  | 
 **body** | [**AuthTokenItemCreateUpdateRequest**](AuthTokenItemCreateUpdateRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_transactions_get**
> object account_transactions_get(page=page, per_page=per_page, type_id=type_id, exclude_type_id=exclude_type_id)

Account transactions history

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
page = 1 # int | Page number (optional) (default to 1)
per_page = 56 # int | Per-page count (default is 15) (optional)
type_id = 'type_id_example' # str | Return only records of these types, comma-separated list of IDs (optional)
exclude_type_id = 'exclude_type_id_example' # str | Exclude records of these types, comma-separated list of IDs (optional)

try:
    # Account transactions history
    api_response = api_instance.account_transactions_get(page=page, per_page=per_page, type_id=type_id, exclude_type_id=exclude_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_transactions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **account_twofa_delete**
> account_twofa_delete(body=body)

Disable Two Factor Authentication (2FA)

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body() # Body |  (optional)

try:
    # Disable Two Factor Authentication (2FA)
    api_instance.account_twofa_delete(body=body)
except ApiException as e:
    print("Exception when calling AccountApi->account_twofa_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [SecurityCode](../README.md#SecurityCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_twofa_post**
> account_twofa_post(body=body)

Enable Two Factor Authentication (2FA)

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body() # Body |  (optional)

try:
    # Enable Two Factor Authentication (2FA)
    api_instance.account_twofa_post(body=body)
except ApiException as e:
    print("Exception when calling AccountApi->account_twofa_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [SecurityCode](../README.md#SecurityCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_twofa_secret_get**
> object account_twofa_secret_get()

Generate secret code to enable Two Factor Authentication (2FA)

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
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(configuration))

try:
    # Generate secret code to enable Two Factor Authentication (2FA)
    api_response = api_instance.account_twofa_secret_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_twofa_secret_get: %s\n" % e)
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

