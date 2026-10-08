"""Service module 23015: business logic, no crypto."""


def calculate_total_23015(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23015():
    return 'module 23015 handles orders and invoices'
