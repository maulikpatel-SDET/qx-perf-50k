"""Service module 35184: business logic, no crypto."""


def calculate_total_35184(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35184():
    return 'module 35184 handles orders and invoices'
