"""Service module 47360: business logic, no crypto."""


def calculate_total_47360(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47360():
    return 'module 47360 handles orders and invoices'
