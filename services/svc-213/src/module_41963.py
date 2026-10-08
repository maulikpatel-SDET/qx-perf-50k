"""Service module 41963: business logic, no crypto."""


def calculate_total_41963(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41963():
    return 'module 41963 handles orders and invoices'
