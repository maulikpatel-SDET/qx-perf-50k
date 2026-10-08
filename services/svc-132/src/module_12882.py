"""Service module 12882: business logic, no crypto."""


def calculate_total_12882(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12882():
    return 'module 12882 handles orders and invoices'
