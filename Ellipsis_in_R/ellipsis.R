
string <- c('a', 'b', 'c', 'd', 'e')

my_function <- function(vector, ...){

    args <- list(...)

    for (i in vector){
        print(i)
    }

    print(args)
}

#################################################
#################################################

my_function <- function(...){

    args <- list(...)

    for (i in 1:length(args)){
        arg <- args[[i]]
        print(sqrt(arg))
    }
}