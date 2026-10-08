"""Service module 26116: business logic, no crypto."""


def calculate_total_26116(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26116():
    return 'module 26116 handles orders and invoices'
