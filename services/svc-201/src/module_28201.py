"""Service module 28201: business logic, no crypto."""


def calculate_total_28201(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28201():
    return 'module 28201 handles orders and invoices'
