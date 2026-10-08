"""Service module 5756: business logic, no crypto."""


def calculate_total_5756(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5756():
    return 'module 5756 handles orders and invoices'
