# swagger_client.BenchmarksApi

All URIs are relative to *https://api2.hiveos.farm/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**farms_farm_id_benchmarks_benchmark_id_delete**](BenchmarksApi.md#farms_farm_id_benchmarks_benchmark_id_delete) | **DELETE** /farms/{farmId}/benchmarks/{benchmarkId} | Delete benchmark
[**farms_farm_id_benchmarks_benchmark_id_get**](BenchmarksApi.md#farms_farm_id_benchmarks_benchmark_id_get) | **GET** /farms/{farmId}/benchmarks/{benchmarkId} | Benchmark info
[**farms_farm_id_benchmarks_delete**](BenchmarksApi.md#farms_farm_id_benchmarks_delete) | **DELETE** /farms/{farmId}/benchmarks | Delete multiple benchmarks
[**farms_farm_id_benchmarks_get**](BenchmarksApi.md#farms_farm_id_benchmarks_get) | **GET** /farms/{farmId}/benchmarks | Get executed benchmarks
[**farms_farm_id_benchmarks_jobs_get**](BenchmarksApi.md#farms_farm_id_benchmarks_jobs_get) | **GET** /farms/{farmId}/benchmarks/jobs | Get available bechmark jobs (algos) that can be run.
[**farms_farm_id_benchmarks_post**](BenchmarksApi.md#farms_farm_id_benchmarks_post) | **POST** /farms/{farmId}/benchmarks | Start new benchmark


# **farms_farm_id_benchmarks_benchmark_id_delete**
> farms_farm_id_benchmarks_benchmark_id_delete(farm_id, benchmark_id)

Delete benchmark

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
api_instance = swagger_client.BenchmarksApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
benchmark_id = 56 # int | 

try:
    # Delete benchmark
    api_instance.farms_farm_id_benchmarks_benchmark_id_delete(farm_id, benchmark_id)
except ApiException as e:
    print("Exception when calling BenchmarksApi->farms_farm_id_benchmarks_benchmark_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **benchmark_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_benchmarks_benchmark_id_get**
> BenchmarkWithResults farms_farm_id_benchmarks_benchmark_id_get(farm_id, benchmark_id)

Benchmark info

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
api_instance = swagger_client.BenchmarksApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
benchmark_id = 56 # int | 

try:
    # Benchmark info
    api_response = api_instance.farms_farm_id_benchmarks_benchmark_id_get(farm_id, benchmark_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BenchmarksApi->farms_farm_id_benchmarks_benchmark_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **benchmark_id** | **int**|  | 

### Return type

[**BenchmarkWithResults**](BenchmarkWithResults.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_benchmarks_delete**
> farms_farm_id_benchmarks_delete(farm_id, body=body)

Delete multiple benchmarks

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
api_instance = swagger_client.BenchmarksApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.IDs() # IDs |  (optional)

try:
    # Delete multiple benchmarks
    api_instance.farms_farm_id_benchmarks_delete(farm_id, body=body)
except ApiException as e:
    print("Exception when calling BenchmarksApi->farms_farm_id_benchmarks_delete: %s\n" % e)
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

# **farms_farm_id_benchmarks_get**
> object farms_farm_id_benchmarks_get(farm_id, worker_id=worker_id)

Get executed benchmarks

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
api_instance = swagger_client.BenchmarksApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
worker_id = 'worker_id_example' # str | Return only records for these workers, comma-separated list of IDs (optional)

try:
    # Get executed benchmarks
    api_response = api_instance.farms_farm_id_benchmarks_get(farm_id, worker_id=worker_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BenchmarksApi->farms_farm_id_benchmarks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **worker_id** | **str**| Return only records for these workers, comma-separated list of IDs | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_benchmarks_jobs_get**
> object farms_farm_id_benchmarks_jobs_get(farm_id, worker_id=worker_id, tags=tags)

Get available bechmark jobs (algos) that can be run.

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
api_instance = swagger_client.BenchmarksApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
worker_id = 56 # int | Worker ID for individual run (optional)
tags = 'tags_example' # str | Tags for batch run. Comma-separated list of Tag IDs. (optional)

try:
    # Get available bechmark jobs (algos) that can be run.
    api_response = api_instance.farms_farm_id_benchmarks_jobs_get(farm_id, worker_id=worker_id, tags=tags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BenchmarksApi->farms_farm_id_benchmarks_jobs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **worker_id** | **int**| Worker ID for individual run | [optional] 
 **tags** | **str**| Tags for batch run. Comma-separated list of Tag IDs. | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **farms_farm_id_benchmarks_post**
> Benchmark farms_farm_id_benchmarks_post(farm_id, body=body)

Start new benchmark

Benchmark can be started on single or multiple workers (only rigs). If `worker_id` is provided - benchmark is started only on this rig, otherwise benchmark is started on all farm's rigs, optionally filtered by `tag_ids`. 

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
api_instance = swagger_client.BenchmarksApi(swagger_client.ApiClient(configuration))
farm_id = 56 # int | 
body = swagger_client.BenchmarkRequest() # BenchmarkRequest |  (optional)

try:
    # Start new benchmark
    api_response = api_instance.farms_farm_id_benchmarks_post(farm_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BenchmarksApi->farms_farm_id_benchmarks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **farm_id** | **int**|  | 
 **body** | [**BenchmarkRequest**](BenchmarkRequest.md)|  | [optional] 

### Return type

[**Benchmark**](Benchmark.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

