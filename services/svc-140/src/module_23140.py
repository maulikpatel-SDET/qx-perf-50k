"""Service module 23140: business logic, no crypto."""


def calculate_total_23140(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23140():
    return 'module 23140 handles orders and invoices'
