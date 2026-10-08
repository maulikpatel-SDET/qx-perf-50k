"""Service module 15662: business logic, no crypto."""


def calculate_total_15662(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15662():
    return 'module 15662 handles orders and invoices'
