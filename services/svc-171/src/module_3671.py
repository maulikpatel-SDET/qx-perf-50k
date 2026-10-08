"""Service module 3671: business logic, no crypto."""


def calculate_total_3671(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3671():
    return 'module 3671 handles orders and invoices'
