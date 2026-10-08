"""Service module 13671: business logic, no crypto."""


def calculate_total_13671(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13671():
    return 'module 13671 handles orders and invoices'
