"""Service module 12574: business logic, no crypto."""


def calculate_total_12574(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12574():
    return 'module 12574 handles orders and invoices'
