"""Service module 39561: business logic, no crypto."""


def calculate_total_39561(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39561():
    return 'module 39561 handles orders and invoices'
