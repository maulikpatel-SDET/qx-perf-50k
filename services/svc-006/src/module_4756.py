"""Service module 4756: business logic, no crypto."""


def calculate_total_4756(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4756():
    return 'module 4756 handles orders and invoices'
