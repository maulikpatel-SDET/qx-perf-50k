"""Service module 27360: business logic, no crypto."""


def calculate_total_27360(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27360():
    return 'module 27360 handles orders and invoices'
