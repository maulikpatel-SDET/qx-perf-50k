"""Service module 19774: business logic, no crypto."""


def calculate_total_19774(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19774():
    return 'module 19774 handles orders and invoices'
