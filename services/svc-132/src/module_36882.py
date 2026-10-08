"""Service module 36882: business logic, no crypto."""


def calculate_total_36882(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36882():
    return 'module 36882 handles orders and invoices'
