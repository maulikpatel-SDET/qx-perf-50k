"""Service module 5553: business logic, no crypto."""


def calculate_total_5553(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5553():
    return 'module 5553 handles orders and invoices'
