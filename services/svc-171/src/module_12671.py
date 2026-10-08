"""Service module 12671: business logic, no crypto."""


def calculate_total_12671(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12671():
    return 'module 12671 handles orders and invoices'
