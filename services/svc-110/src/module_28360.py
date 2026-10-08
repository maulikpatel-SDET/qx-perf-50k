"""Service module 28360: business logic, no crypto."""


def calculate_total_28360(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28360():
    return 'module 28360 handles orders and invoices'
