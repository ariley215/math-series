def fibonacci(n):
    """
    Calculate the nth Fibonacci number.

    Parameters:
    - n (int): The position of the Fibonacci number to be calculated.

    Returns:
    int: The nth Fibonacci number.
    """
    return n if n <= 1 else fibonacci(n - 2) + fibonacci(n - 1)

def lucas(n):
    """
    Calculate the nth Lucas number.

    Parameters:
    - n (int): The position of the Lucas number to be calculated.

    Returns:
    int: The nth Lucas number.
    """
    return 2 if n == 0 else 1 if n == 1 else lucas(n - 2) + lucas(n - 1)

def other_series(n):
    """
    Calculate the nth number in another series.

    Parameters:
    - n (int): The position of the number in the series to be calculated.

    Returns:
    int: The nth number in the other series.
    """
    return 3 if n == 0 else 4 if n == 1 else other_series(n - 2) + other_series(n - 1)

def sum_series(n, first_num=0, sec_num=1):
    """
    Calculate the nth number in a series based on the first and second numbers provided.

    Parameters:
    - n (int): The position of the number in the series to be calculated.
    - first_num (int): The first number in the series.
    - sec_num (int): The second number in the series.

    Returns:
    int: The nth number in the specified series.
    """
    if first_num == 0 and sec_num == 1:
        return fibonacci(n)
    if first_num == 2 and sec_num == 1:
        return lucas(n)
    if first_num == 3 and sec_num == 4:
        return other_series(n)

print(sum_series(2, 2, 1), sum_series(6, 3, 4))

  
  
#######################IN CLASS REVIEW###########################################
  
# def lucas(n):
#     return 2 if n == 0 else 1 if n == 1 else lucas(n - 2) + lucas(n - 1)

# def other_series(n):
#     return 3 if n == 0 else 4 if n == 1 else other_series(n - 2) + other_series(n - 1)

# def sum_series(n, first_num=0, sec_num=1):
#     if first_num == 0 and sec_num == 1:
#         return fibonacci(n)
#     if first_num == 2 and sec_num == 1:
#         return lucas(n)
#     if first_num == 3 and sec_num == 4:
#         return other_series(n)

# print(sum_series(2, 2, 1), sum_series(6, 3, 4))