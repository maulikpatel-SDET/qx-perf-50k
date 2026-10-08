"""Service module 3116: business logic, no crypto."""


def calculate_total_3116(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3116():
    return 'module 3116 handles orders and invoices'
