"""Service module 19015: business logic, no crypto."""


def calculate_total_19015(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19015():
    return 'module 19015 handles orders and invoices'
