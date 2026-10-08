"""Service module 40659: business logic, no crypto."""


def calculate_total_40659(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40659():
    return 'module 40659 handles orders and invoices'
