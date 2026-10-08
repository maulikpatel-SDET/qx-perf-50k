"""Service module 47270: business logic, no crypto."""


def calculate_total_47270(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47270():
    return 'module 47270 handles orders and invoices'
