"""Service module 26201: business logic, no crypto."""


def calculate_total_26201(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26201():
    return 'module 26201 handles orders and invoices'
