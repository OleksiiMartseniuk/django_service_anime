def cash_memory(func):
    """ Кэширования данных """
    data = {}

    def wrapper(*args, **kwargs):
        if data.get(f'{args[1]}'):
            return data.get(f'{args[1]}')
        else:
            result = func(*args, **kwargs)
            data[result.title] = result
            return result

    def cache_clear():
        # Очистка кеша
        nonlocal data
        data = {}

    wrapper.cache_clear = cache_clear
    return wrapper
