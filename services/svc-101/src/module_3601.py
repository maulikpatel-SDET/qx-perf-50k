"""Service module 3601: business logic, no crypto."""


def calculate_total_3601(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3601():
    return 'module 3601 handles orders and invoices'
