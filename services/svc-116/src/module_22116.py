"""Service module 22116: business logic, no crypto."""


def calculate_total_22116(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22116():
    return 'module 22116 handles orders and invoices'
