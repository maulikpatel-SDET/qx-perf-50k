"""Service module 20444: business logic, no crypto."""


def calculate_total_20444(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20444():
    return 'module 20444 handles orders and invoices'
