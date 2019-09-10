from functools import reduce


def moving_chunks(s, size):
    for slice_start in range(0, len(s)):
        if slice_start + size <= len(s):
            yield s[slice_start:slice_start + size]


def largest_product(series, size):
    products = []
    if size < 0:
        raise ValueError(".+")
    if len(series) == 0 and size != 0:
        raise ValueError(".+")
    if len(series) == 0 and size == 0:
        return 1
    c = list(moving_chunks(series, size))
    for chunk in c:
        product = reduce(lambda x, y: x * y, (int(digit) for digit in chunk), 1)
        products.append(product)
    return max(products)
