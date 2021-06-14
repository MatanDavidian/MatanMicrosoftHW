# MatanMicrosoftHW

# Matan resource group
the group contain two ARM:
1. Storage_ARM with two storage accounts(source, destination)
2. Server_ARM a windows server, where "Server script" can run from.

# Server script
## before run
Before run the script please:
1. change the path in the files script.bat and run.py(script_path varible in copy_blobs_between_storage_accounts function)
2. unzip azcopy.rar in the current directory
## description
the script create 100 blob files upload them to source storage account, and then copy them from source storage account to destination storage account
