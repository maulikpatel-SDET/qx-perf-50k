"""Service module 35671: business logic, no crypto."""


def calculate_total_35671(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35671():
    return 'module 35671 handles orders and invoices'
