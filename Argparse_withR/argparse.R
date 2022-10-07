#!/usr/bin/env Rscript

library(argparse)

parser <- ArgumentParser(description="An executible script to practice using command line R scripts")

parser$add_argument("-n", "--name", type="character", dest="name", help="Provide a name", required=TRUE)

parser$add_argument("-a", "--age", type="integer", dest="age", help="Provide an age", required=TRUE)


args <- parser$parse_args()

name <- args$name
age <- args$age 

print(paste0('Hi. My name is ', name, ' and I am ', age, ' years old.'))