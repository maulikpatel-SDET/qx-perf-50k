"""Service module 20360: business logic, no crypto."""


def calculate_total_20360(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20360():
    return 'module 20360 handles orders and invoices'
