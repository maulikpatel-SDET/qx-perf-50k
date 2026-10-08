"""Service module 23693: business logic, no crypto."""


def calculate_total_23693(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23693():
    return 'module 23693 handles orders and invoices'
