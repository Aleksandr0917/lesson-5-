def is_prime(funk):
    def wrapper(*args, **kwargs):
        result = funk(*args, **kwargs)
        sum_ = sum(args)

        return  result
    
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)



result = sum_three(2, 3, 6)
print(result)