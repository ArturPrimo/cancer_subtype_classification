# Steps for Reproducing Results in Feature Selection Project

## 1. Downloading the Requirements on *requirements.txt*

### a. It is recommended to create a virtual environment for a new project on Python. If you'd like to do so, search up how to create and activate one on your preffered terminal or shell.

### b. Run: *pip install -r requirements.txt* to install all packages listed on file.

## 2. Downloading Data and Prreprocessing Data

### a. Run download.R to generate a dataset for the sample labels and cancer subtype information, this is what is stored on *cancer_subtypes.csv*

### b. Run download_genes.R three times to generate three datasets named *tcga_brca.csv*, *tcga_coad.csv*, *tcga_prad.csv*. For each run of the R file, be sure to change the commented names and values for each of the datasets to reproduce three different csv's. Be sure to have all your packages listed at the start of each of the R files installed. 

### c. Merge both values by running *data_cleaner.py* to join the *cancer_subtypes.csv* with each of the *tcga_brca.csv*, *tcga_coad.csv*, *tcga_prad.csv* to reproduce values that are workable.

## 3. Run Experiment

### a. Running a simple: *python feature_selection.py* does the trick. During the running of the code, you are able to observe the confusion matrices being generated. 

### b. The data is saved on the data folder under *feature_selection_results.csv*.

### c. To replicate the bar plots seen on the report, simply run *plots.py*

## Bonus: visualise_data.ipynb is a playground for visualizing anything necessary and to inspect data formats for instance. Can be modified and used for other visualization purposes as well.