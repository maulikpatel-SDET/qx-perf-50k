"""Service module 41270: business logic, no crypto."""


def calculate_total_41270(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41270():
    return 'module 41270 handles orders and invoices'
