"""Service module 38553: business logic, no crypto."""


def calculate_total_38553(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38553():
    return 'module 38553 handles orders and invoices'
