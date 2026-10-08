"""Service module 7116: business logic, no crypto."""


def calculate_total_7116(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7116():
    return 'module 7116 handles orders and invoices'
