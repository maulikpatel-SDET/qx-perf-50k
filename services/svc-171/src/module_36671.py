"""Service module 36671: business logic, no crypto."""


def calculate_total_36671(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36671():
    return 'module 36671 handles orders and invoices'
