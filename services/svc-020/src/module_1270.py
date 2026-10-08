"""Service module 1270: business logic, no crypto."""


def calculate_total_1270(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1270():
    return 'module 1270 handles orders and invoices'
