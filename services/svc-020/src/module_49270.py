"""Service module 49270: business logic, no crypto."""


def calculate_total_49270(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49270():
    return 'module 49270 handles orders and invoices'
