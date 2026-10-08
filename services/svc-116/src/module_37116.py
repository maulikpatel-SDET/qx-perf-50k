"""Service module 37116: business logic, no crypto."""


def calculate_total_37116(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37116():
    return 'module 37116 handles orders and invoices'
