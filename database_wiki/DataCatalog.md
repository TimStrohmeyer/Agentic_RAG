### Curated Zone

Schema Name: emea_cz
#### Dimensions

Last update: 2024.05.09
| Table Name | Associated Dimensions | Description |
|:--|:--|:--|
|dbid_billing_document|  |Contains descriptive information about billing documents, payment status payment terms, and detailing transaction dates. |
|dacc_account|  |Holds account information including account status, type and structure.|
|dcus_dm_80_customer_v|  |Contains customer information like demographies, geograhpies, industires and company wide classifications. |
|dmat_material_v|  |Contains material master information containing details on materials, such as descriptions, categories and weight information.|
|dpor_purchase_order|  |Contains Purchase Order information like receiving, preparation and shipping dates, vendor, shipper and receiver details as well as references to the content of the Purchase.|

Last update: 2024.05.10
#### Fact
| Table Name | Associated Dimensions | Description |
|:--|:--|:--|
|fcur_currency_rate_hyperion|dcur_currency|Stores currency exchange rates, and links the reference date, scenario, and rate type.|
|ffco_cooo_cooc|  |Contains details of cost center operations, including cost allocations and related financials and links the relevant customers and dates.|
|finv_dm_95_snapshot_after_kitting_base|  |Snapshot table capturing state of inventory post-kitting process, holding information about inventory balances and links materials and dates.|
|fpor_dm_80_billed_purchase_order_all_v|dpor_purchase_order|Contains all billed purchase orders their amount and value and links to the cusomter, shipping center and date information.|