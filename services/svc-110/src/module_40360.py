"""Service module 40360: business logic, no crypto."""


def calculate_total_40360(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40360():
    return 'module 40360 handles orders and invoices'
