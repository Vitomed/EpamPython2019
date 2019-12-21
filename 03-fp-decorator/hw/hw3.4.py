import time
from functools import wraps


def make_cache_with_arg_version1(decorator_time=3):
    """Stores the result of the function over time time_live

    Saves the results of previous function calls in its
    storage for a certain time, which is passed as an
    argument to the decorator"""

    def decorator(func):
        #  I am a cache and I will be created at the time of decorating the function
        storage_function_value = {}
        @wraps(func)
        def inner(*args, **kwargs):
            key = args + tuple(sorted(kwargs.items()))  # dict is unhashable
            try:
                time_is_over = time.perf_counter() - storage_function_value[args][-1] > decorator_time
            except KeyError:
                create_cache = list(func(*args, **kwargs))
                create_cache.append(time.monotonic())
                storage_function_value[key] = create_cache
                return create_cache, "New, just created cache"
            else:
                if not time_is_over:
                    return storage_function_value[args], "From cache"
                else:
                    new_cache_value = list(func(*args, **kwargs))
                    new_cache_value.append(time.monotonic())
                    storage_function_value[args] = new_cache_value
                    return new_cache_value, "New, with cache replacement"
        return inner
    return decorator


@make_cache_with_arg_version1(3)
def slow_func(*args, **kwargs):
    if kwargs:
        for value in args:
            yield value, kwargs
    else:
        for value in args:
            yield value


ar = (1,2,3)
kw = {"1": 1, "0": 0, "5+": 5}
print("make_cache_with_arg_version1")
print(slow_func(*ar, **kw))
time.sleep(1)
print(slow_func("three"))
print(slow_func("one"))
time.sleep(4)
print(slow_func("three"))


def make_cache_with_arg_version2(decorator_time):
    """Stores the result of the function over time time_live

    Saves the results of previous function calls in its
    storage for a certain time, which is passed as an
    argument to the decorator"""


    def decorator(func):
        #  I am a cache and I will be called only once when you ask me to create a decorator for you.
        storage_function_value = {}  # {args: [result, time]}
        @wraps(func)
        def inner(*args, **kwargs):
            key = args + tuple(sorted(kwargs.items()))  # dict is unhashable
            if key in storage_function_value and \
                    time.perf_counter() - storage_function_value[args][-1] < decorator_time:
                return storage_function_value[key], "From cache"
            create_cache = list(func(*args, **kwargs))
            create_cache.append(time.perf_counter())
            storage_function_value[key] = create_cache
            return create_cache, "New created cache"

        return inner
    return decorator


@make_cache_with_arg_version2(3)
def slow_func(*args, **kwargs):
    if kwargs:
        for value in args:
            yield value, kwargs
    else:
        for value in args:
            yield value


# ar = (1,2,3)
# kw = {"1": 1, "0": 0, "5+": 5+}
#
# print("make_cache_with_arg_version2")
# print(slow_func(*ar, **kw))
# time.sleep(1)
# print(slow_func("three"))
# print(slow_func("one"))
# time.sleep(4)
# print(slow_func("three"))
