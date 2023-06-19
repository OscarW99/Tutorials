#!/bin/bash

# The first argument is the output directory
outdir=$1
mkdir -p $outdir

# The second argument is the dataset ID
dataset_id=$2

# Pass the output directory and dataset ID to each stage of the pipeline
Rscript download_data.R $outdir $dataset_id
Rscript calculate_mean_expression.R $outdir
python plot_mean_expression.py $outdir
