# WorkerEditRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] [default to True]
**tag_ids** | **list[int]** |  | [optional] 
**tag_update_mode** | **str** | Update mode for tags * add - add spicified tags ignoring if already assigned; * remove - remove spicified tags if assigned; * replace - replace all assigned tags with specified ones;  | [optional] [default to 'replace']
**mirror_url** | [**MirrorUrl**](MirrorUrl.md) |  | [optional] 
**vpn** | **object** | VPN configuration  Files will be named as following, so certificates in client.conf should be named ca.crt, client.crt, client.key.  Also you can embed certificates in client.conf and upload just one file.  | [optional] 
**fs_id** | **int** | Flight sheet ID | [optional] 
**oc_id** | **int** | Overclocking profile ID | [optional] 
**oc_apply_mode** | **str** | How to apply overclocking profile: - replace - means copy entire per-brand configurations of both default and per-algo sets; - merge - means copy only individual fields of per-brand configurations of both default and per-algo sets.  | [optional] [default to 'replace']
**oc_config** | [**OCConfig**](OCConfig.md) |  | [optional] 
**oc_algo** | [**OCAlgo**](OCAlgo.md) |  | [optional] 
**miners_config** | [**MinersConfig**](MinersConfig.md) |  | [optional] 
**watchdog** | **object** | Watchdog system | [optional] 
**options** | **object** | Worker options. This object will be merged with existing one on update.  | [optional] 
**hardware_power_draw** | **int** | Power consumption of worker&#39;s hardware, watts | [optional] 
**psu_efficiency** | **int** | Efficiency of power supply unit, % | [optional] 
**octofan_correct_power** | **bool** | Apply power correction settings to power consumption value from Octominer fan controller. Default is false. | [optional] 
**autofan** | **object** | Autofan configuration | [optional] 
**octofan** | **object** | Configuration for Octominer fan controller | [optional] 
**coolbox** | **object** | Configuration for Coolbox fan controller | [optional] 
**fanflap** | **object** | Configuration for FanFlap controller | [optional] 
**powermeter** | **object** | Configuration for Powermeter controller | [optional] 
**donnager_relay** | **object** | Donnager Relay configuration | [optional] 
**ykeda_autofan** | **object** | Configuration for Ykeda Autofan controller | [optional] 
**asic_config** | **dict(str, str)** | Settings for ASICs with Hive firmware, depends on model and firmware version | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


