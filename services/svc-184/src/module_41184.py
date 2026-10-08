"""Service module 41184: business logic, no crypto."""


def calculate_total_41184(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41184():
    return 'module 41184 handles orders and invoices'
