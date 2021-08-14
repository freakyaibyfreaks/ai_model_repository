"""
Provides options via the command line to perform project tasks.
* `--data_source`: dataset to be downloaded from the storage (bentham, iam, rimes, saintgall, washington)
"""

import argparse
import sys

# Adding parent's path
sys.path.append('../../')

from utils.s3_download import DownloadData

BUCKET_NAME = 'data-handwritten-model' # Bucket name

# Dataset and name mapping
dataset_enum = ['bentham','iam', 'rimes', 'saintgall', 'washington']

# # Dataset and file mapping
dataset_file_mapping = {
    'bentham' : 'bentham.zip',
    'iam' : 'iam.zip',
    'rimes' : 'rimes.zip',
    'saintgall' : 'saintgall.zip',
    'washington' : 'washington.zip'
}

# main code
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=str, required=True)
 
    # Extracting all the arguments
    args = parser.parse_args()
     
    # raise exception if values is not present
    if args.source in dataset_enum:
    
        # create the object of the class
        download_data = DownloadData()

        # Download the file
        download_data.get_file(BUCKET_NAME, dataset_file_mapping[args.source])
        
        # Unzip the file
        download_data.unzip_file(dataset_file_mapping[args.source])
    else:
        raise ValueError('Error!! Unexpected value found. Kindly refer README.md')

