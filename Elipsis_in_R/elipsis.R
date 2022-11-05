
my_vec <- c(1,2,3,4,5,6,7,8,9,10)

test_function <- function(vector, ...){

    extra_arguments <- list(...)

    for (i in 1:length(extra_arguments)){
        assign(x = names(extra_arguments)[i], value = extra_arguments[[i]])
    }

    ls()

    # for (i in vector){
    #     print(i)
    # }

    print(extra_arguments)
}






new_function <- function(...){

    for (arg in list(...)){

        square <- sqrt(arg)
        print(square)
    }
}




















