"""Service module 4553: business logic, no crypto."""


def calculate_total_4553(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4553():
    return 'module 4553 handles orders and invoices'
