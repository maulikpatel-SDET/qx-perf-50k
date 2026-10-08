"""Service module 18444: business logic, no crypto."""


def calculate_total_18444(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18444():
    return 'module 18444 handles orders and invoices'
