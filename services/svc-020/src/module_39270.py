"""Service module 39270: business logic, no crypto."""


def calculate_total_39270(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39270():
    return 'module 39270 handles orders and invoices'
