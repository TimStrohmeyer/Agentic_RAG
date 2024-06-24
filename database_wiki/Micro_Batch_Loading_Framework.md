# Micro Batch Loading Framework for the Curated Zone



New transactions are constantly being added to the Standardized Zone and are created with a HKey and a timestamp.

The transaction timestamp always ascends. So, if the highest currently-extracted timestamp is known, it’s easy to select only the newer transactions. This is the fundamental technique underpinning the SQL query which extracts new records from the SZ.

At any point in time the replicated data will be slightly out-of-date compared to the SZ schema, due to the new transactions which have just been added. Every small batch adds a small increment of transactions to the replicated table.

Over time, doing this repeatedly will accumulate a large amount of data. However the individual data loads only need to deal with a small number of rows. This makes the incremental data extraction very fast, and enables the microbatching to keep very close to real time.

## Components
![CR_MicroBatchLoadingFramework-Microbatch Loading Framework.png](/.attachments/CR_MicroBatchLoadingFramework-Microbatch%20Loading%20Framework-be44c700-f08c-4bbb-b826-adfcd374895a.png)

### Dependency Configuration
- Map of Source Tables to Job Names in table stored in synpase
- Matillion Jobs are only allowed to depend on Vaultspeed Jobs, all other dependencies should be as Views in Synapse to reduce complexity - exception refernece tables - Job dependency in Matillion also work but should not be considered in the feature.
- All jobs must be driven by a „driving“ source table. This source table defines the delta records to be loaded. The "driving" source tables are mapped in the last_source_table column of the [TABLE_LINEAGE](/Data-Lineage).

### Standardized Zone Pipeline Notifier
- Each job loading a Vaultspeed source must notify the update time windows of the last data load
- Notification must be an asynchronous job to decouple architecture building blocks (here Vaultspeed and Matillion)
- Notification steps in the pipeline should be created automatically (e.g. by the CI/CD pipeline) and not be coded by the developers.
- Design Option 1) Notification steps issues a message to Blob storage queue with the source table name and the earliest timestamp of the micro batch
- Design Option 2) Notification steps issues a message to Blob storage queue with the target Matillion Job Name based on the Dependency Configuration and the earliest timestamp of the micro batch

### Matillion Job Orchestration
- Matillion listens on the Blob storage queue and triggers an Orchestration Job
- Design Option 1)
	- Table for Dependency Configuration is loaded
	- Get source table from pipeline notification event and look up target Matillion job via grid variable
	- Call target Matillion job and pass earliest micro batch timestamp to target job as job variable

### Matillion target job requirements
- each target job has a variable for earliest micro batch timestamp
- The default timestamp „1900-01-01 00:00:00“ is treated as full load
- each target job has a driving table (or a join/union of tables) where a filter is applied to the data vault satellites: load timestamp >= earliest micro batch timestamp

### Prerequisites
- Azure Blob storage queue configured
- Matillion project is setup to listen on Blobl Storage queue
- Table lineage is with for the latest statest of the DEV/UAT/PRD environments (VaultSpeed and Matillion metadata are joined and up-to-date, Table lineage automation requires matillion git repository and AzureDevOps Pipeline)
- python is installed on the Matillion machine


![OBIS DnA DataFlow (1).png](/.attachments/OBIS%20DnA%20DataFlow%20(1)-099b9cc7-aa26-4871-bacf-1a90041cb68f.png)