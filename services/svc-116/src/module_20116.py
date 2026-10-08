"""Service module 20116: business logic, no crypto."""


def calculate_total_20116(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20116():
    return 'module 20116 handles orders and invoices'
