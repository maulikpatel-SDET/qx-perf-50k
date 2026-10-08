"""Service module 35270: business logic, no crypto."""


def calculate_total_35270(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35270():
    return 'module 35270 handles orders and invoices'
