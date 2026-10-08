"""Service module 14116: business logic, no crypto."""


def calculate_total_14116(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14116():
    return 'module 14116 handles orders and invoices'
