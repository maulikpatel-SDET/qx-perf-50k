"""Service module 25444: business logic, no crypto."""


def calculate_total_25444(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25444():
    return 'module 25444 handles orders and invoices'
