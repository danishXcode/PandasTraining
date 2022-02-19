# Wallet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coin** | **str** | Coin name | [optional] 
**name** | **str** | Display name | [optional] 
**wal** | **str** |  | [optional] 
**source** | **str** | Wallet source. Can be either exchange name or any string. For supported exchanges see /hive/wallet_sources endpoint.  | [optional] 
**fetch_balance** | **bool** | Try to retrieve wallet balance from blockchain or exchange | [optional] [default to False]
**api_key_id** | **int** | ID of attached API key for balance fetching (if required) | [optional] 
**balance** | **object** | Wallet balance info. Either balance or status is present, not both. Pending status indicates that the balance is fetching at the moment and will be available soon. Other statuses indicate balance cannot be fetched. Balance info is cached by 30 minutes.  | [optional] 
**pool_balances** | **list[object]** | Balances from pools that this wallet uses | [optional] 
**fs_count** | **int** | Amount of flight sheets that use this wallet | [optional] 
**workers_count** | **int** | Amount of workers that use this wallet | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


