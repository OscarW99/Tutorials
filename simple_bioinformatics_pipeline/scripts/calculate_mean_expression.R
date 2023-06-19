#!/usr/bin/env Rscript

# Load required libraries
library(tidyverse)

# Check command line arguments
args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 1) {
  stop("You must provide one command line argument: output directory")
}

# Get the output directory from command line arguments
outdir <- args[1]

# Load the expression data
expression_data <- read.csv(file = paste0(outdir, "/expression_data.csv"))

# Calculate the mean expression for each gene
mean_expression <- rowMeans(expression_data[-1])

# Save the mean expression values
write.csv(data.frame(gene = rownames(expression_data), mean_expression = mean_expression),
          file = paste0(outdir, "/mean_expression.csv"))
