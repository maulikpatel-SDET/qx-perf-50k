"""Service module 10015: business logic, no crypto."""


def calculate_total_10015(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10015():
    return 'module 10015 handles orders and invoices'
