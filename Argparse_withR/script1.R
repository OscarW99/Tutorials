#!/usr/bin/env Rscript

library(argparse)

parser <- ArgumentParser(description='An executible script to practice using command line R scripts')

parser$add_argument("-n", "--name", type="character", dest="name", help="Provide a name")
parser$add_argument("-a", "--age", type="integer", dest="age", help="Provide an age")
# This overwrites a commandline argument with the same 'dest'
parser$add_argument("test", help="Testing Testing")

args <- parser$parse_args('test')
args2 <- parser$parse_args('whbedbw')


parser$print_help()

# TODO.. add 'required = TRUE/ FALSE test
