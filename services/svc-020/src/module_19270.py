"""Service module 19270: business logic, no crypto."""


def calculate_total_19270(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19270():
    return 'module 19270 handles orders and invoices'
