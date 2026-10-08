"""Service module 35553: business logic, no crypto."""


def calculate_total_35553(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35553():
    return 'module 35553 handles orders and invoices'
