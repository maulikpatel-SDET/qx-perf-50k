"""Service module 5270: business logic, no crypto."""


def calculate_total_5270(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5270():
    return 'module 5270 handles orders and invoices'
