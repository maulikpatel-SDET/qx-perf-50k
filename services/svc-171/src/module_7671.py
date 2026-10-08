"""Service module 7671: business logic, no crypto."""


def calculate_total_7671(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7671():
    return 'module 7671 handles orders and invoices'
