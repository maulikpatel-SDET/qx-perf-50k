"""Service module 3463: business logic, no crypto."""


def calculate_total_3463(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3463():
    return 'module 3463 handles orders and invoices'
