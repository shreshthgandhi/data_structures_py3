# Introduction

Notes for [Python Decorators 101](https://realpython.com/primer-on-python-decorators/)

What is a decorator?
 - A function that takes another function.
 - Extends the behaviour of that function
 - Without explicitly modifying the function
 
## Functions as First Class Objects
 Functions are first class objects in Python.
  - Can be passed around into lists
  - Can be passed as arguments to other functions
  

 ```python
def say_hello(name):
    return f"Hello {name}"


def say_goodbye(name):
    return f"Goodbye {name}"

# Passing a function as an object
def greet_person(greeter_func):
    return greeter_func("Bob")
```

The `greet_person` function expects a function as its argument
```python
>>> greet_person(say_hello)
'Hello Bob'
>>> greet_person(say_goodbye)
'Goodbye Bob'
```

## Returning Functions from Functions

```python
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
```
The parent function returns a reference to an inner function.
```python
>>> first()
'First Child'
>>> second()
'Second Child'
```
`first` and `second` can be used like regular functions even though 
the `first_child` and `second_child` functions can't be accessed from the outside scope.

## Simple Decorators

```python
def my_decorator(func):
    def wrapper():
        print('Pre-execution action')
        func()
        print('Post-execution action')
    return wrapper

def say_hello():
    print("Hello Bob")
```
```python
>>> say_hello = my_decorator(say_hello)
>>> say_hello()
Pre-execution action
Hello Bob
Post-execution action
```

## Template for a decorator
 - Using `*args` and `**kwargs` in the inner wrapper function allows us to deal with functions with arbitrary arguments.
 - The @functools.wraps decorator preserves information (such as name and documentation) for 
the original function being decorated.

```python
import functools

def decorator(func):
    @functools.wraps(func):
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
```



