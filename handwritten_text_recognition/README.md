## This repo contains all the code and requirements of the handwritten model

### Download data
1. Download the dataset
   a) cd handwritten_text_recognition && cd raw
   b) python3 download.py --source $data-source
    
      Currently these 5 values are allowed in $data-source
        1) bentham
        2) iam
        3) rimes(Inprogress)
        4) saintgall
        5) washington

2. To preprocess, encode and save the transformed data into **data** folder.
   
   a) cd .. && cd handwritten_text_recognition && cd src
   b) python3 covert_data_to_hdf5.py --source=<DATASET_NAME> --transform

    
