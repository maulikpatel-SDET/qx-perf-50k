"""Service module 38116: business logic, no crypto."""


def calculate_total_38116(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38116():
    return 'module 38116 handles orders and invoices'
