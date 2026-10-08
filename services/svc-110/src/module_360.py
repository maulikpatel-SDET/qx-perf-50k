"""Service module 360: business logic, no crypto."""


def calculate_total_360(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_360():
    return 'module 360 handles orders and invoices'
