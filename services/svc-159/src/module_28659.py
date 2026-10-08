"""Service module 28659: business logic, no crypto."""


def calculate_total_28659(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28659():
    return 'module 28659 handles orders and invoices'
