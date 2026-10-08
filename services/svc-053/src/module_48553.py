"""Service module 48553: business logic, no crypto."""


def calculate_total_48553(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48553():
    return 'module 48553 handles orders and invoices'
