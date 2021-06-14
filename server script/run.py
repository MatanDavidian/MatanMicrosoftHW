import subprocess
from time import sleep
import os, uuid
import shutil
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

# Print azure.storage.blob version
print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

# Global vars
blob_files_amount = 100
src_container_name = "mysrccontainer"
local_path = "./data"
# Get source storage key token for upload files
connect_str_src = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
blob_service_client_src = BlobServiceClient.from_connection_string(connect_str_src)


def create_and_upload_files(amount):
    def upload_files(local_file_name, upload_file_path):
        blob_client = blob_service_client_src.get_blob_client(container=src_container_name, blob=local_file_name)
        print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)
        # Upload the created file
        with open(upload_file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
            
    if os.path.exists(local_path):
        shutil.rmtree(local_path)
    os.mkdir(local_path)
    # Create a files in the local data directory to upload
    for i in range(amount):
        local_file_name =   f"Matan{i}.txt"
        upload_file_path = os.path.join(local_path, local_file_name)
        # Write text to the file
        file = open(upload_file_path, 'w')
        file.write("Hello World, it's file number:{i}\n")
        file.close()
        upload_files(local_file_name, upload_file_path)


def copy_blobs_between_storage_accounts(amount):
    script_path = r"C:\inetpub\wwwroot\my_script\script.bat"
    for i in range(amount):   
        subprocess.Popen(script_path + f" Matan{i}.txt Matan{i}.txt")
        sleep(2)


def create_src_container():
    blob_service_client_src.create_container(src_container_name)


def main():
    # Create source container if not exist
    try:
        blob_service_client_src.create_container(src_container_name)
        sleep(2)
    except:
        print("src container already exists")
    # Create and upload files to containers
    create_and_upload_files(blob_files_amount)
    # Create files from src container to destination container
    copy_blobs_between_storage_accounts(blob_files_amount)

if __name__ == '__main__':
    main()
