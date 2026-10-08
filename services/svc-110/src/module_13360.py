"""Service module 13360: business logic, no crypto."""


def calculate_total_13360(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13360():
    return 'module 13360 handles orders and invoices'
