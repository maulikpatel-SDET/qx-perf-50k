"""Service module 15270: business logic, no crypto."""


def calculate_total_15270(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15270():
    return 'module 15270 handles orders and invoices'
