def function_a():
    print("Function A started")
    function_b()
    print("Function A ended")

def function_b():
    print("Function B started")
    function_c()
    print("Function B ended")

def function_c():
    print("Function C started")
    # Intentional Error
    # result = 10 / 0
    # debug it
    result = 10 / 1
    print("Function C ended")

# call the initial function
function_a()