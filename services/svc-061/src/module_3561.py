"""Service module 3561: business logic, no crypto."""


def calculate_total_3561(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3561():
    return 'module 3561 handles orders and invoices'
