"""Service module 32671: business logic, no crypto."""


def calculate_total_32671(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32671():
    return 'module 32671 handles orders and invoices'
