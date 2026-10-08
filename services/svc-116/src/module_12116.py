"""Service module 12116: business logic, no crypto."""


def calculate_total_12116(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12116():
    return 'module 12116 handles orders and invoices'
