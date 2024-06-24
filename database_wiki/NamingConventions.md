[[_TOC_]] 

# Database & Schemas
|Entity|Topic|Abbreviation|Reference|
|---|---|---|---|
|Database|User|PROJECT_ENVIRONMENT_LAYER_WORD|5-10 digits ≠ <>*#.%&:\\+?/|
|Database|Warehouse|PROJECT_ENVIRONMENT_LAYER_WH||
|Database|Database|PROJECT_ENVIRONMENT_DB||
|Database|Schema|PROJECT_LAYER_WORD||
|Database|Trigger Prefix|TR|5-10 digits ≠ <>*#.%&:\\+?/|
|Database|Schedule Prefix|RUN|5-10 digits ≠ <>*#.%&:\\+?/|
|Environment|Schedule Prefix|DEV|Devlopement environment|
|Environment|Schedule Prefix|UAT|User accepting test environment|
|Environment|Schedule Prefix|RUN|Production environment|
|Dataflow Layer|Raw Zone|RZ|Staged source tables|
|Dataflow Layer|Standardized Zone|SZ|DataVault tables|
|Dataflow Layer|Curated Zone|CZ|DataMart tables|

# Tables
- Table name in Data Vault: - Example: HUB_ORDER
- Table name in Data Mart: - Example DORD_ORDER
- All tables contain one attribute with suffix _HKEY (Table name_HKEY; e.g. DORD_ORDER_HKEY) Uwhich contains the HK of the respective source (Satellite)
- All tables contain a attribute load_date which contains the date of the gration of the row. For the datamart the load_date from the Vault will be taken

|Entity|Topic|Abbreviation|Reference|
|---|---|---|---|
|Table prefix|Satellite|SAT||
|Table prefix|Computed satellites|CSAT||
|Table prefix|Hub|HUB||
|Table prefix|Link|LNK||
|Table prefix|Link satellite|LKS||
|Table prefix|Dimension|DIM||
|Table prefix|Bridge|BRG||
|Table prefix|Facttable|F||
|Table prefix|PIT|PIT||
|Table prefix|External table|EXT||
|Table prefix|Temporary tables|TMP||
|Table prefix|Materialized view|MV||
|Table prefix|Views|V||

# VaultSpeed
|Entity|Topic|Abbreviation|Reference|
|---|---|---|---|
|VaultSpeed Schema|FL|[PROJECT]_[LAYER]_FL|1-128 digits ≠ <>*#.%&:\\+?/|
|VaultSpeed Schema|CDC|[PROJECT]_[LAYER]_CDC_[SOURCE]|1-128 digits ≠ <>*#.%&:\\+?/|
|VaultSpeed Schema|FMC|[PROJECT]_[LAYER]_FMC|1-128 digits ≠ <>*#.%&:\\+?/|
|VaultSpeed Schema|MTD|[PROJECT]_[LAYER]_MTD_[SOURCE]|1-128 digits ≠ <>*#.%&:\\+?/|
|VaultSpeed Schema|BV|[PROJECT]_[LAYER]_BV_[SOURCE]|1-128 digits ≠ <>*#.%&:\\+?/|
|VaultSpeed Schema|DFV|[PROJECT]_[LAYER]_DFV_[SOURCE]|1-128 digits ≠ <>*#.%&:\\+?/|
|VaultSpeed Schema|FL_MIGRATION|[PROJECT]_[LAYER]_FL_MIGRATION_[SOURCE]|1-128 digits ≠ <>*#.%&:\\+?/|
|VaultSpeed Schema|EXT|[PROJECT]_[LAYER]_EXT_[SOURCE]|1-128 digits ≠ <>*#.%&:\\+?/|
|VaultSpeed Schema|INI|[PROJECT]_[LAYER]_INI_[SOURCE]|1-128 digits ≠ <>*#.%&:\\+?/|
|VaultSpeed Schema|PROC|[PROJECT]_[LAYER]_PROC|1-128 digits ≠ <>*#.%&:\\+?/|
|VaultSpeed Schema|STG|[PROJECT]_[LAYER]_STG_[SOURCE]|1-128 digits ≠ <>*#.%&:\\+?/|

# Matillion

## Columns
- Column names in SNAKE_CASE - Example: ORDER_DATE

|Entity|Topic|Abbreviation|Reference|
|---|---|---|---|
|Column Suffix|HASH KEY attributes (hash key, binary, varbinary)|HKEY||
|Column Suffix|TIMESTAMP attributes (timestamp)|TIMESTAMP||
|Column Suffix|TIME attributes (time)|TIME||
|Column Suffix|DATE attributes (date)|DATE||
|Column Suffix|Describing attributes (description)|DESC||
|Column Suffix|German language attributes (in german)|GER||
|Column Suffix|English language attributes (in english)|ENG||
|Column Suffix|Code attributes (code, sign, id)|ID||
|Column Suffix|Flag attribute (Flag number)|FG||
|Column Suffix|Percentage attribute (percentage)|PCT||
|Column Suffix|Number attribute (number)|NO||
|Column Suffix|Temporary|TMP||
|Column Suffix|Document Currency (number)|DC||
|Column Suffix|Local Currency (number)|LC||
|Column Suffix|Euro Currency (number)|EC||

## Jobs
- Job names in SNAKE_CASE - Example: TRN_F_SALES

|Entity|Topic|Abbreviation|Reference|
|---|---|---|---|
|Job Prefix|Transformation|TRN|Transformation in Matillion|
|Job Prefix|Shared Jobs|SHR|Shared Jobs in Matillion|
|Pipeline|Orchestration|ORC|Orchestration in Matillion|

## Variables
- Variables in SNAKE_CASE - Example: E_SCHEMA_CZ

|Entity|Topic|Abbreviation|Reference|
|---|---|---|---|
|Job variable|Prefix|J||
|Job variable|Suffix|C|Copied|
|Job variable|Suffix|S|Shared|
|grid variable|Prefix|G||
|grid variable|Suffix|C|Copied|
|grid variable|Suffix|S|Shared|
|Environment variable|Prefix|E||
|Environment variable|suffix|C|Copied|
|Environment variable|suffix|S|Shared|
## Environment Variables
All of them are type _text_ and have a _shared_ behaviour

|Name|OLY_EMEA_OBIS_DEV|
|---|---|
|E_EMEA_ADLS_STORAGE|eudevstgobis|
|E_EMEA_BLOB_CON_STAGING|eudevconsf|
|E_EMEA_SCHEMA_CREF|emea_obis_bv|
|E_EMEA_SCHEMA_CSATS|emea_obis_bv|
|E_EMEA_SCHEMA_CZ|emea_cz|
|E_EMEA_SCHEMA_CZ_TMP|emea_cz_tmp|
|E_EMEA_SCHEMA_REF|emea_obis_ref_fl|
|E_EMEA_SCHEMA_SZ|emea_obis_dv_fl|
|E_EMEA_SCHEMA_SZ_BV|emea_obis_bv|
|E_EMEA_SCHEMA_TECHSUP|emea_cz_techsup|

## GiT Branches
|Entity|Topic|Abbreviation|Reference|
|---|---|---|---|
|Git|Branch to solve user story|FXXXX/USXXXXX||
|Git|Branch to solve bugs|FXXXX/BFXXXX||

## Components
- Component names in CamelCase - Example: JnrOrderPartner

|Entity|Topic|Abbreviation|Reference|
|---|---|---|---|
|SQL Documentation|FUNCTIONAL_SCENARIO|WordWord|Describes the part of the statement added to the job|
|SQL Documentation|Aggregate Component|Agg[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Assert View Component|Ast[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Calculator Component|Cal[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Construct Struct Component|Cns[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Construct Variant|Cnv[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Convert Type Component|Cnt[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Delete Rows Component|Del[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Detect Changes Component|Dtc[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Distinct Component|Dis[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Extract Nested Data|Exn[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Filter Component|Flt[FUNCTIONAL_SCENARIO]||
|SQL Documentation|First/Last Component|Fnl[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Flatten Variant Component|Ftv[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Lead/Lag Component|Lnl[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Map Values Component|Mpv[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Pivot Component|Pvt[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Rank Component|Rnk[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Rename Component|Ren[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Replicate Component|Rep[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Split Field Component|Spl[FUNCTIONAL_SCENARIO]||
|SQL Documentation|SQL Component|Sql[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Transpose Columns|Trc[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Transpose Rows|Trr[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Window Calculation Component|Wic[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Unpivot Component|Unp[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Join Component|Jon[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Unite Component|UNI_[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Intersect Component|Int[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Except Component|Exc[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Fixed Flow Component|Fxf[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Generate Sequence Component|Seq[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Multi Table Input Component|Mtb[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Stream Input|Sti[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Table Input Component|Tbi[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Wildcard Table Input|Wit[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Copy Table To External Schema|Cpt[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Create View Component|Crv[FUNCTIONAL_SCENARIO]||
|SQL Documentation|External Table Output|Ext[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Rewrite Table Component|Wrt[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Rewrite External Table|Wre[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Table Output Component|Tbo[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Table Update Component|Tbu[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Assert External Table Component|Aet[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Assert Scalar Variables Component|Avt[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Assert Table Component|Ast[FUNCTIONAL_SCENARIO]||
|SQL Documentation|API Extract|Api[FUNCTIONAL_SCENARIO]||
|SQL Documentation|API Query|Apq[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Azure SQL Query|Azq[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Azure Blob Storage Load|Azb[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Azure Blob Storage Unload|Azu[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Create External Table|Cet[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Create Table Component|Crt[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Delete Tables Component|Del[FUNCTIONAL_SCENARIO]||
|SQL Documentation|SQL Script Component|Sqc[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Truncate Tables Component|Trt[FUNCTIONAL_SCENARIO]||
|SQL Documentation|File Iterator Component|Fit[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Fixed Iterator Component|Fxi[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Grid Iterator Component|Gri[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Loop Iterator|Lop[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Table Iterator Component|Tbi[FUNCTIONAL_SCENARIO]||
|SQL Documentation|And Component|And[FUNCTIONAL_SCENARIO]||
|SQL Documentation|End Failure Component|Enf[FUNCTIONAL_SCENARIO]||
|SQL Documentation|End Success Component|Ens[FUNCTIONAL_SCENARIO]||
|SQL Documentation|If component|If[FUNCTIONAL_SCENARIO]||
|SQL Documentation|OR component|Or[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Retry Component|Ret[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Run Orchestration Component|Ror[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Run Transformation Component|Rtr[FUNCTIONAL_SCENARIO]||
|SQL Documentation|Python Script Component|Pys[FUNCTIONAL_SCENARIO]||

# Qlik Replicate
Qlik Replicate Tasks and Endpoints are following the naming convention predefined in DnA project.  

## Qlik Replicate Endpoint Naming convention
The following factors are considered while arriving at this format.  
1. There are two types of endpoints in Qlik Replicate.  Source & Target.
2. Three environments in DnA - DEV, UAT & PRD
3. Category of the source or the target system - SYN, ADLS, SAPEXT, ORA, IDB2, LDB2, SQL for Azure Synapse, Data Lake storage, SAP Extractor, Oracle, IBM DB2 on iSeries, IBM DB2 on Linux and MS SQL respectively
4. Name of the Application - OURANUS, JUPITER, RZ (Raw Zone), NEOGAIACRM, NEOGAIAECC etc. 

Some examples are given below.
- TARGET-DEV-SYN-RZ
- SOURCE-UAT-SAPEXT-OEKGCRM
- TARGET-PRD-ADLS-OBIS
- SOURCE-DEV-IDB2-SALES
- SOURCE-UAT-SQL-HFM
- SOURCE-PRD-ORA-EBS

## Qlik Replicate Task Naming convention
The following factors are considered while arriving at this format.  
1. There could be multiple tasks for the same pair of source and target endpoints. Some tables loaded using task1 & other tables using task2.  
2. Name of the application in-line with the Source endpoint.  

Some examples are given below.
- TASK-DEV-OEKGCRM-01
- TASK-DEV-OSTECCEXT-01
- TASK-DEV-JUPSAPDB-01
- TASK-DEV-MBCSAPEXT-02
- TASK-DEV-HFM-01
# Theobald
## Schemas
| Source        | Description                                        | Target Schema |
|---------------|----------------------------------------------------|---------------|
| SAP CRM       | Customer Relationship Management Module            | RZ_SAPCRM 
| SAP CRM Ref   | Reference tables from Customer Relationship Module | RZ_SAPCRM_REF
| SAP OW Par    | Logistics Partner information from SAP OW System   | RZ_SAPOW_PAR
| SAP OE Par    | Logistics Partner Information from SAP OE system   | RZ_SAPOE_PAR
| SAP OE MM Pur | Materials Management Purchasing from SAP OE System | RZ_SAPOE_MMPUR
| SAP OW MM Pur | Materials Management Purchasing from SAP OW System |RZ_SAPOW_MMPUR
| SAP OE SD     | Sales and Distribution from SAP OE System          | RZ_SAPOE_SD
| SAP OW SD     | Sales and Distribution from SAP OW System          |RZ_SAPOW_SD
| SAP OE MM | Materials Management from SAP OE System | RZ_SAPOE_MM
|SAP OW MM| Materials Management from SAP OW System | RZ_SAPOW_MM
| SAP OE FICO | Financial Accounting and Controlling from SAP OE system | RZ_SAPOE_FICO
| SAP OW FICO | Financial Accounting and Controlling from SAP OW system |RZ_SAPOW_FICO
| SAP OE REF | Reference data from SAP OE System module-overarching | RZ_SAPOE_REF
|SAP OW REF | Reference data from SAP OW System module-overraching |RZ_SAPOW_FICO|

## Extraction naming

System abbreviation + Table or extractor name + Interval name (If partitioned on a date field)

In general, most of the extractions are partitioned on a date field they have and it is either monthly, quarterly or yearly.

### Exceptions
1. For the sources that had to be partitioned but didn't have any date field,  below convention has been used.

System abbreviation + Table or extractor name + Sequenced integers

2. Data from CDPOS table has been filtered on TABNAME (Table name columns). Naming convention follows

System abbreviation + CDPOS + TABNAME filter

### Examples    
- OE_MBEW_2022 -> Points to MBEW table 2022 in the OEP system.
- OC_STXH_2017_H2 -> Points to STXH table 2017 second half in the OCP system.
- OW_JCDS_2020_Q4 -> Points to JCDS table 2020 last quarter in the OWP system.  
- OC_ZCRM_CONDITIONS_2020_12 -> Points to ZCRM_CONDITIONS extractor for last month of 2012.
- OE_LTAP_1 -> Partitioned on document number field. Points to first bucket.
- OW_CDPOS_LIKP -> Extracts data with 'LIKP' in TABNAME column.

## Destination folders and files naming

Every extraction is written as a parquet file in the BLOB storage. Naming of these folders and files is configured in Theobald. Rules are;
1. Every extraction must have a folder name on its SAP Object name.
3. Non-partitioned extractions must use SAP object name as the file name.
2. Partitions should use name of the extractions as the file name. 

![image.png](/.attachments/image-9f208ca9-8309-4f77-aba8-1bb3549465a3.png)

# Reference Data

Reference Data is used for mappings in data integration process.

Use schema to manage reference data that is not managed by source systems.
RZ_REFDATA

Table name starts with ‘REF_’

- Contains at least this attributes


```
Code varchar notnull

Value varchar notnull

```

- Always define a default value (code according to standardized zone ghost records)

- Can contain additional attributes for

  - Defining harmonized target code

  - Grouping values or parent child identifiers

  - Descriptions

  - Sort orders

  - Alternative texts

  - Translations to other languages

- Must contain technical attributes for

  - Created_DATE datetime

  - Modified_DATE datetime

  - Modified_User varchar

  - Valid_FROM (if history must be maintained) datetime

  - Valid_TO  (if history must be maintained) datetime

Code is the business key, not a hashkey. Code is used in the dimension or fact tables. Value is the text that is shown in the reports.

# Parameter Data

Parameter Data is managing functionality on any front end application or business process. Parameter data maintained in the schema RZ_REFDATA and tables will start with PARAM_
