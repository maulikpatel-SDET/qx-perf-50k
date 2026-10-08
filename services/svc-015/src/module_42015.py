"""Service module 42015: business logic, no crypto."""


def calculate_total_42015(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42015():
    return 'module 42015 handles orders and invoices'
