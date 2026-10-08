"""Service module 29774: business logic, no crypto."""


def calculate_total_29774(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29774():
    return 'module 29774 handles orders and invoices'
