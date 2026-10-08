"""Service module 5444: business logic, no crypto."""


def calculate_total_5444(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5444():
    return 'module 5444 handles orders and invoices'
