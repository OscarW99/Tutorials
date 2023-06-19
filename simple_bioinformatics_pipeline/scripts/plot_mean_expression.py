#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import sys

# Check command line arguments
if len(sys.argv) != 2:
    sys.exit("You must provide one command line argument: output directory")

# Get the output directory from command line arguments
outdir = sys.argv[1]

# Load the mean expression data
df = pd.read_csv(f'{outdir}/mean_expression.csv')

# Create the plot
plt.hist(df['mean_expression'], bins=50)

# Label the plot
plt.xlabel('Mean Expression')
plt.ylabel('Frequency')

# Save the plot
plt.savefig(f'{outdir}/mean_expression_histogram.png')
