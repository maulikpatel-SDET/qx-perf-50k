"""Service module 44180: business logic, no crypto."""


def calculate_total_44180(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44180():
    return 'module 44180 handles orders and invoices'
