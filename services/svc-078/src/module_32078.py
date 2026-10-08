"""Service module 32078: business logic, no crypto."""


def calculate_total_32078(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32078():
    return 'module 32078 handles orders and invoices'
