# TransactionAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Transaction ID | [optional] 
**timestamp** | **int** | Transaction timestamp | [optional] 
**type_id** | [**TransactionTypeAccount**](TransactionTypeAccount.md) |  | [optional] 
**amount** | **float** | Transaction amount | [optional] 
**currency** | **str** | Transaction currency | [optional] 
**amount_fiat** | **float** | Transaction amount in fiat currency | [optional] 
**cost_details** | [**list[TransactionCostItem]**](TransactionCostItem.md) | Cost details for type 2. | [optional] 
**referral_user** | **object** | Referral user for type 3 | [optional] 
**comment** | **str** | Comment for type 4 | [optional] 
**txid** | **str** | Coinpayments transaction ID for type 1, or blockchain transaction ID for type 5  | [optional] 
**txurl** | **str** | Blockchain transaction explore URL for type 5 | [optional] 
**target_user** | **object** | Target user for type 6 | [optional] 
**source_user** | **object** | Source user for type 7 | [optional] 
**target_farm** | **object** | Target farm for types 2, 10 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


