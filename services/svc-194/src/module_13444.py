"""Service module 13444: business logic, no crypto."""


def calculate_total_13444(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13444():
    return 'module 13444 handles orders and invoices'
