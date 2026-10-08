"""Service module 21116: business logic, no crypto."""


def calculate_total_21116(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21116():
    return 'module 21116 handles orders and invoices'
