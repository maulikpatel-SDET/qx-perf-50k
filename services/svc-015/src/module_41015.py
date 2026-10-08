"""Service module 41015: business logic, no crypto."""


def calculate_total_41015(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41015():
    return 'module 41015 handles orders and invoices'
