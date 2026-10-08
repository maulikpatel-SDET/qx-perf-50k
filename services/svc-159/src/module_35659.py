"""Service module 35659: business logic, no crypto."""


def calculate_total_35659(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35659():
    return 'module 35659 handles orders and invoices'
