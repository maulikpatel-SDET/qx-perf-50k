"""Service module 116: business logic, no crypto."""


def calculate_total_116(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_116():
    return 'module 116 handles orders and invoices'
