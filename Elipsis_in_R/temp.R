
my_vec <- c(1,2,3,4,5,6,7,8,9,10)

test_function <- function(vector, ...){
    print(...)
    extra_arguments <- list(...)

    for (i in vector){
        print(i)
    }

    print(extra_arguments) #!
}

test_function(my_vec, 2, 3, 4, 5)

# ctrl Q ctrl Enter 

# Assign elipsis arguments to list rather than vector incase we have different data types (vector can hold only one data type).


my_ellipsis_function <- function(...) {

    args <- list(...)

    for(i in 1:length(args)) {
        assign(x = names(args)[i], value = args[[i]])
    }

    ls() # show the available variables

    # some other code and operations
    # that use the ellipsis-arguments as “native” variables…
}

my_ellipsis_function(some_number = 123, some_string = 'abc')