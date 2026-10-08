"""Service module 30650: business logic, no crypto."""


def calculate_total_30650(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30650():
    return 'module 30650 handles orders and invoices'
