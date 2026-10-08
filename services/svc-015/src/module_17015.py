"""Service module 17015: business logic, no crypto."""


def calculate_total_17015(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17015():
    return 'module 17015 handles orders and invoices'
