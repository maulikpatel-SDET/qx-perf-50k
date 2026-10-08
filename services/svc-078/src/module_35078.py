"""Service module 35078: business logic, no crypto."""


def calculate_total_35078(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35078():
    return 'module 35078 handles orders and invoices'
