"""Service module 22750: business logic, no crypto."""


def calculate_total_22750(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22750():
    return 'module 22750 handles orders and invoices'
