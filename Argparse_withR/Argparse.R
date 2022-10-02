#!/usr/bin/env Rscript

libary(argpasre)

parser <- ArgumentParser(description="An executible script to practice using command line R scripts")

parser$add_argument("-n", "--name", type="character", dest="name", help="Provide a name")



