"""Service module 29685: business logic, no crypto."""


def calculate_total_29685(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29685():
    return 'module 29685 handles orders and invoices'
