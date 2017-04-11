# KnowEnG's Gene Signature Pipeline
 This is the Knowledge Engine for Genomics (KnowEnG), an NIH BD2K Center of Excellence, Gene Signature Pipeline.

  
* * * 
## How to run this pipeline with Our data
* * * 
###1. Get Access to KnowEnG-Research Repository:
Email omarsobh@illinois.edu infrastructure team (IST) lead to:

* __Access__ KnowEnG-Research github repo

###2. Clone the Gene_Signature Repo
```
 git clone https://github.com/KnowEnG-Research/Gene_Signature.git
```
 
###3. Install the following (Ubuntu or Linux)
```
 apt-get install -y python3-pip
 apt-get install -y libblas-dev liblapack-dev libatlas-base-dev gfortran
 pip3 install numpy==1.11.1
 pip3 install pandas==0.18.1
 pip3 install scipy==0.18.0
 pip3 install scikit-learn==0.17.1
 apt-get install -y libfreetype6-dev libxft-dev
 pip3 install matplotlib==1.4.2
 pip3 install pyyaml
 pip3 install knpackage
 pip3 install redis
```

###4. Change directory to Gene_Signature

```
cd Gene_Signature 
```

###5. Change directory to test

```
cd test
```
 
###6. Create a local directory "run_dir" and place all the run files in it
```
make env_setup
```

###7. Use following "make" commands to run a gene signature pipeline
```
make run_cosine_similarity
```


* * * 
## How to run this pipeline with Your data
* * * 

__***Follow steps 1-4 above then do the following:***__

### * Create your run directory

 ```
 mkdir run_directory
 ```

### * Change directory to the run_directory

 ```
 cd run_directory
 ```

### * Create your results directory

 ```
 mkdir results_directory
 ```
 
### * Create run_paramters file  (YAML Format)
 ``` 
Look for examples of run_parameters in ./Gene_Signature/data/run_files/TEMPLATE_gene_signature.yml
 ```
### * Modify run_paramters file  (YAML Format)
```
set the spreadsheet file names to point to your data
```

### * Run the Gene Signature Pipeline:

  * Update PYTHONPATH enviroment variable
   ``` 
   export PYTHONPATH='../src':$PYTHONPATH    
   ```
   
  * Run
   ```
  python3 ../src/gene_signature.py -run_directory ./ -run_file TEMPLATE_gene_signature.yml
   ```

* * * 
## Description of "run_parameters" file
* * * 

| **Key**                   | **Value** | **Comments** |
| ------------------------- | --------- | ------------ |
| method                    | cosine_similarity | Calculate cosine similarity between two gene expression data |
| spreadsheet_name_full_path_1 | directory+spreadsheet_name|  Path and file name of user supplied gene expression data  |
| spreadsheet_name_full_path_2 | directory+spreadsheet_name| Path and file name of our supplied ggene expression data  |
| results_directory | directory | Directory to save the output files |

spreadsheet_name_full_path_1 = gene_spreadsheet_1.tsv</br>
spreadsheet_name_full_path_2 = gene_spreadsheet_2.tsv 

* * * 
## Description of Output files saved in results directory
* * * 

* Output files


**gene_signature_cos_similarity.tsv**.</br>

|  | sheet1_sample_1 | ... | sheet1_sample_i |
|:---------:|:---------:|:---------:| :---------:|
| sheet2_sample_1 | 1 | 0 | 0 |
| ... | ... | ... | ... | 
| sheet2_sample_j | 0 | 0 | 1 |

