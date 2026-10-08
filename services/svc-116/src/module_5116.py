"""Service module 5116: business logic, no crypto."""


def calculate_total_5116(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5116():
    return 'module 5116 handles orders and invoices'
