

# Inner Functions

def parent(num):
    def first_child():
        return "First Child"
    def second_child():
        return "Second Child"

    if num == 1:
        # Return a reference to the inner function first_child
        return first_child
    else:
        return second_child

first = parent(1)
second = parent(2)