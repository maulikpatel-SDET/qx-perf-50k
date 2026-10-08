"""Service module 31756: business logic, no crypto."""


def calculate_total_31756(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31756():
    return 'module 31756 handles orders and invoices'
