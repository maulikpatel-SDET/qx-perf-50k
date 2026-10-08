"""Service module 31444: business logic, no crypto."""


def calculate_total_31444(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31444():
    return 'module 31444 handles orders and invoices'
