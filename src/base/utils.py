def cash_memory(func):
    """ Кэширования данных """
    data = {}

    def wrapper(*args, **kwargs):
        if data.get(f'{args[1].title}'):
            return data.get(f'{args[1].title}')
        else:
            result = func(*args, **kwargs)
            data[f'{args[1].title}'] = result
            return result
    return wrapper
