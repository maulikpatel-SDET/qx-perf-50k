"""Service module 7940: business logic, no crypto."""


def calculate_total_7940(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7940():
    return 'module 7940 handles orders and invoices'
