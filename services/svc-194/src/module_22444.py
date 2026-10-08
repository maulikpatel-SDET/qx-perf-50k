"""Service module 22444: business logic, no crypto."""


def calculate_total_22444(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22444():
    return 'module 22444 handles orders and invoices'
