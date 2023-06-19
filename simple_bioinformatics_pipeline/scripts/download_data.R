#!/usr/bin/env Rscript

# Load required libraries
library(Biobase)
library(GEOquery)

# Check command line arguments
args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 2) {
  stop("You must provide two command line arguments: output directory and dataset ID")
}

# Get the output directory and GEO ID from command line arguments
outdir <- args[1]
geo_id <- args[2]

# Fetch the data from GEO database
gset <- getGEO(geo_id, GSEMatrix =TRUE, getGPL=FALSE)

# Check if data download was successful
if (is.null(gset)) {
  stop("Failed to download data from GEO database")
}

# If there are multiple datasets, use the first one
if (is.list(gset)) {
  gset <- gset[[1]]
}

# Get the expression data and round to integers
expression_data <- round(exprs(gset))

# Save the data for further usage
write.csv(expression_data, file = paste0(outdir, "/expression_data.csv"))
