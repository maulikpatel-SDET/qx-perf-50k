"""Service module 4116: business logic, no crypto."""


def calculate_total_4116(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4116():
    return 'module 4116 handles orders and invoices'
