"""Service module 3351: business logic, no crypto."""


def calculate_total_3351(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3351():
    return 'module 3351 handles orders and invoices'
