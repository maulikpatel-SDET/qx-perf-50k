"""Service module 22015: business logic, no crypto."""


def calculate_total_22015(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22015():
    return 'module 22015 handles orders and invoices'
